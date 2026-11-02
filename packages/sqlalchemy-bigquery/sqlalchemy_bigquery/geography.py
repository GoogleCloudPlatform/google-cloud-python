# Copyright (c) 2021 The PyBigQuery Authors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import geoalchemy2
import geoalchemy2.functions
import sqlalchemy.ext.compiler
from geoalchemy2.shape import to_shape
from shapely import wkb, wkt
from sqlalchemy.sql.elements import BindParameter

SRID = 4326  # WGS84, https://spatialreference.org/ref/epsg/wgs-84/


class WKB(geoalchemy2.WKBElement):
    """
    Well-Known-Binary data wrapper.

    WKB objects hold geographic data in a binary format known as
    "Well-Known Binary",
    <https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry>.
    These objects are returned from queries and can be used in insert
    and queries.

    The WKB class is a subclass of the Geoalchemy2 WKBElement class
    customized for working with BigQuery.
    """

    geom_from_extended_version = "ST_GeogFromWKB"

    def __init__(self, data):
        super().__init__(data, SRID, True)

    @property
    def wkt(self):
        """
        Return the WKB object as a WKT object.
        """
        return WKT(to_shape(self).wkt)


class WKT(geoalchemy2.WKTElement):
    """
    Well-Known-Text data wrapper.

    WKT objects hold geographic data in a text format known as
    "Well-Known Text",
    <https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry>.

    You generally shouldn't need to create WKT objects directly, as
    text arguments to geographic functions and inserts to GEOGRAPHY
    columns are automatically coerced to geographic data.

    The WKT class is a subclass of the Geoalchemy2 WKTElement class
    customized for working with BigQuery.
    """

    geom_from_extended_version = "ST_GeogFromText"

    def __init__(self, data):
        super().__init__(data, SRID, True)

    @property
    def wkb(self):
        """
        Return the WKT object as a WKB object.
        """
        return WKB(wkb.dumps(wkt.loads(self.data)))


class GEOGRAPHY(geoalchemy2.Geography):
    """
    GEOGRAPHY type

    Use this to define BigQuery GEOGRAPHY columns::

        class Lake(Base):
            __tablename__ = 'lakes'

            name = Column(String)
            geog = column(GEOGRAPHY)

    See https://googleapis.dev/python/sqlalchemy-bigquery/latest/geography.html
    """

    def __init__(self):
        super().__init__(
            geometry_type=None,
            spatial_index=False,
            srid=SRID,
        )
        self.extended = True

    # Un-inherit the bind function that adds an ST_GeogFromText.
    # It's unnecessary and causes BigQuery to error.
    #
    # Some things to note about this:
    #
    # 1. bind_expression can't always know the value.  When multiple
    #    rows are being inserted, the values may be different in each
    #    row.  As a consequence, we have to treat all the values as WKT.
    #
    # 2. This applies equally to explicitly converting with
    #    st_geogfromtext, or implicitly with the geography parameter
    #    conversion.
    #
    # 3. We handle different types using bind_processor, below.
    #
    bind_expression = sqlalchemy.sql.type_api.TypeEngine.bind_expression

    def bind_processor(self, dialect):
        """
        SqlAlchemy plugin that controls how values are converted to parameters

        When we bind values, we always bind as text.  We have to do
        this because when we decide how to bind, we don't always know
        what the values will be.

        This is not a user-facing method.
        """

        def process(bindvalue):
            if isinstance(bindvalue, WKT):
                return bindvalue.data
            elif isinstance(bindvalue, WKB):
                return bindvalue.wkt.data
            else:
                return bindvalue

        return process

    @staticmethod
    def ElementType(data, srid=SRID, extended=True):
        """
        Plugin for the Geoalchemy2 framework for constructing WKB objects.

        The framework wants a callable, which it assumes is a class
        (this the name), for constructing a geographic element.

        We don't want `WKB` to accept extra arguments that it checks
        and ignores, so we do that in this wrapper.

        This is not a user-facing method.
        """
        if srid != SRID:
            raise AssertionError("Bad srid", srid)
        if not extended:
            raise AssertionError("Extended must be True.")
        return WKB(data)


@sqlalchemy.ext.compiler.compiles(geoalchemy2.functions.GenericFunction, "bigquery")
def _fixup_st_arguments(element, compiler, **kw):
    """
    Compiler-plugin for the BigQuery that overrides how geographic functions are handled

    Geographic function (ST_...) get turned into
    `geoalchemy2.functions.GenericFunction` objects by
    Geoalchemy2. The code here overrides how they're handeled.

    We want arguments passed to have the GEOGRAPHY type associated
    with them, when appropriate, where "when appropriate" is
    determined by the `function documentation
    <https://cloud.google.com/bigquery/docs/reference/standard-sql/geography_functions>`_..

    This is not a user-facing function.
    """
    argument_types = _argument_types.get(element.name.lower())
    if argument_types:
        for argument_type, argument in zip(argument_types, element.clauses.clauses):
            if isinstance(argument, BindParameter) and not isinstance(
                argument.type, argument_type
            ):
                argument.type = argument_type()

    return compiler.visit_function(element, **kw)


_argument_types = dict(
    st_area=(GEOGRAPHY,),
    st_asbinary=(GEOGRAPHY,),
    st_asgeojson=(GEOGRAPHY,),
    st_astext=(GEOGRAPHY,),
    st_boundary=(GEOGRAPHY,),
    st_centroid=(GEOGRAPHY,),
    st_centroid_agg=(GEOGRAPHY,),
    st_closestpoint=(
        GEOGRAPHY,
        GEOGRAPHY,
    ),
    st_clusterdbscan=(GEOGRAPHY,),
    st_contains=(
        GEOGRAPHY,
        GEOGRAPHY,
    ),
    st_convexhull=(GEOGRAPHY,),
    st_coveredby=(
        GEOGRAPHY,
        GEOGRAPHY,
    ),
    st_covers=(
        GEOGRAPHY,
        GEOGRAPHY,
    ),
    st_difference=(
        GEOGRAPHY,
        GEOGRAPHY,
    ),
    st_dimension=(GEOGRAPHY,),
    st_disjoint=(
        GEOGRAPHY,
        GEOGRAPHY,
    ),
    st_distance=(
        GEOGRAPHY,
        GEOGRAPHY,
    ),
    st_dump=(GEOGRAPHY,),
    st_dwithin=(
        GEOGRAPHY,
        GEOGRAPHY,
    ),
    st_endpoint=(GEOGRAPHY,),
    st_equals=(
        GEOGRAPHY,
        GEOGRAPHY,
    ),
    st_exteriorring=(GEOGRAPHY,),
    st_geohash=(GEOGRAPHY,),
    st_intersection=(
        GEOGRAPHY,
        GEOGRAPHY,
    ),
    st_intersects=(
        GEOGRAPHY,
        GEOGRAPHY,
    ),
    st_intersectsbox=(GEOGRAPHY,),
    st_iscollection=(GEOGRAPHY,),
    st_isempty=(GEOGRAPHY,),
    st_length=(GEOGRAPHY,),
    st_makeline=(
        GEOGRAPHY,
        GEOGRAPHY,
    ),
    st_makepolygon=(
        GEOGRAPHY,
        GEOGRAPHY,
    ),
    st_makepolygonoriented=(GEOGRAPHY,),
    st_maxdistance=(
        GEOGRAPHY,
        GEOGRAPHY,
    ),
    st_npoints=(GEOGRAPHY,),
    st_numpoints=(GEOGRAPHY,),
    st_perimeter=(GEOGRAPHY,),
    st_pointn=(GEOGRAPHY,),
    st_simplify=(GEOGRAPHY,),
    st_snaptogrid=(GEOGRAPHY,),
    st_startpoint=(GEOGRAPHY,),
    st_touches=(
        GEOGRAPHY,
        GEOGRAPHY,
    ),
    st_union=(
        GEOGRAPHY,
        GEOGRAPHY,
    ),
    st_union_agg=(GEOGRAPHY,),
    st_within=(
        GEOGRAPHY,
        GEOGRAPHY,
    ),
    st_x=(GEOGRAPHY,),
    st_y=(GEOGRAPHY,),
)

__all__ = ["GEOGRAPHY", "WKB", "WKT"]
