from google.cloud import documentai
from google.cloud.documentai_toolbox.converters.config import bbox_conversion
from google.cloud.documentai_toolbox.converters.config.block import Block


def test_midpoint_in_bpoly():
    vertex_a = documentai.NormalizedVertex(x=2, y=2)
    box_a = documentai.BoundingPoly(normalized_vertices=[vertex_a])

    vertex_b = documentai.NormalizedVertex(x=1, y=1)
    vertex_b_max = documentai.NormalizedVertex(x=4, y=4)
    box_b = documentai.BoundingPoly(normalized_vertices=[vertex_b, vertex_b_max])

    actual = bbox_conversion._midpoint_in_bpoly(box_a=box_a, box_b=box_b)
    assert actual


def test_merge_text_anchors():
    text_segment_1 = documentai.Document.TextAnchor.TextSegment(
        start_index="0", end_index="100"
    )
    text_anchor_1 = documentai.Document.TextAnchor(text_segments=[text_segment_1])

    text_segment_2 = documentai.Document.TextAnchor.TextSegment(
        start_index="100", end_index="200"
    )
    text_anchor_2 = documentai.Document.TextAnchor(text_segments=[text_segment_2])

    text_segment_3 = documentai.Document.TextAnchor.TextSegment(
        start_index="0", end_index="200"
    )
    expected = documentai.Document.TextAnchor(text_segments=[text_segment_3])
    actual = bbox_conversion._merge_text_anchors(
        text_anchor_1=text_anchor_1, text_anchor_2=text_anchor_2
    )
    assert actual == expected


def test_get_text_anchor_in_bbox():
    vertex_a = documentai.NormalizedVertex(x=2, y=2)
    vertex_a_max = documentai.NormalizedVertex(x=5, y=5)
    box_a = documentai.BoundingPoly(normalized_vertices=[vertex_a, vertex_a_max])

    vertex_b = documentai.NormalizedVertex(x=1, y=1)
    vertex_b_max = documentai.NormalizedVertex(x=8, y=8)
    box_b = documentai.BoundingPoly(normalized_vertices=[vertex_b, vertex_b_max])

    text_segment_1 = documentai.Document.TextAnchor.TextSegment(
        start_index="0", end_index="100"
    )
    text_anchor_1 = documentai.Document.TextAnchor(text_segments=[text_segment_1])

    text_segment_2 = documentai.Document.TextAnchor.TextSegment(
        start_index="100", end_index="200"
    )
    text_anchor_2 = documentai.Document.TextAnchor(text_segments=[text_segment_2])

    layout1 = documentai.Document.Page.Layout(
        bounding_poly=box_b, text_anchor=text_anchor_1
    )
    layout2 = documentai.Document.Page.Layout(
        bounding_poly=box_b, text_anchor=text_anchor_2
    )

    token1 = documentai.Document.Page.Token(layout=layout1)
    token2 = documentai.Document.Page.Token(layout=layout2)

    page = documentai.Document.Page(tokens=[token1, token2])
    actual = bbox_conversion.get_text_anchor_in_bbox(bbox=box_a, page=page)

    text_segment_3 = documentai.Document.TextAnchor.TextSegment(
        start_index="0", end_index="200"
    )
    expected = documentai.Document.TextAnchor(text_segments=[text_segment_3])
    assert actual == expected


def test_get_norm_x_max():
    vertex_a_min = documentai.NormalizedVertex(x=2, y=2)
    vertex_a_max = documentai.NormalizedVertex(x=4, y=4)

    bbox = documentai.BoundingPoly(normalized_vertices=[vertex_a_min, vertex_a_max])
    actual = bbox_conversion._get_norm_x_max(bbox=bbox)
    assert actual == 4


def test_get_norm_x_min():
    vertex_a_min = documentai.NormalizedVertex(x=2, y=2)
    vertex_a_max = documentai.NormalizedVertex(x=4, y=4)

    bbox = documentai.BoundingPoly(normalized_vertices=[vertex_a_min, vertex_a_max])
    actual = bbox_conversion._get_norm_x_min(bbox=bbox)
    assert actual == 2


def test_get_norm_y_max():
    vertex_a_min = documentai.NormalizedVertex(x=2, y=2)
    vertex_a_max = documentai.NormalizedVertex(x=4, y=4)

    bbox = documentai.BoundingPoly(normalized_vertices=[vertex_a_min, vertex_a_max])
    actual = bbox_conversion._get_norm_y_min(bbox=bbox)
    assert actual == 2


def test_get_norm_y_min():
    vertex_a_min = documentai.NormalizedVertex(x=2, y=2)
    vertex_a_max = documentai.NormalizedVertex(x=4, y=4)

    bbox = documentai.BoundingPoly(normalized_vertices=[vertex_a_min, vertex_a_max])
    actual = bbox_conversion._get_norm_y_max(bbox=bbox)
    assert actual == 4


def test_normalize_coordinates():
    actual = bbox_conversion._normalize_coordinates(x=4.0, y=2.0)
    assert actual == 2.0


def test_convert_to_pixels():
    actual = bbox_conversion._convert_to_pixels(x=1, conversion_rate=96)
    assert actual == 96


def test_convert_bbox_units_with_normalized():
    actual = bbox_conversion._convert_bbox_units(
        coordinate=0.5, input_bbox_units="normalized", width=2550, height=3300
    )
    assert actual == 0.5


def test_convert_bbox_units_with_pxl():
    actual = bbox_conversion._convert_bbox_units(
        coordinate=1, input_bbox_units="pxl", width=2550, height=3300
    )
    assert actual == 0.000392157


def test_convert_bbox_units_with_inch():
    actual = bbox_conversion._convert_bbox_units(
        coordinate=1, input_bbox_units="inch", width=2550, height=3300
    )
    assert actual == 0.037647059


def test_convert_bbox_units_with_cm():
    actual = bbox_conversion._convert_bbox_units(
        coordinate=1, input_bbox_units="cm", width=2550, height=3300
    )
    assert actual == 0.014821569


def test_get_multiplier_pxl():
    actual = bbox_conversion._get_multiplier(
        docproto_coordinate=1000, external_coordinate=1000, input_bbox_units="pxl"
    )
    assert actual == 1.0


def test_get_multiplier_inch():
    actual = bbox_conversion._get_multiplier(
        docproto_coordinate=1000, external_coordinate=10.416, input_bbox_units="inch"
    )
    assert actual == 1.000064004096262


def test_get_multiplier_cm():
    actual = bbox_conversion._get_multiplier(
        docproto_coordinate=1000, external_coordinate=26.4585, input_bbox_units="cm"
    )
    assert actual == 1.000000992500985


def test_convert_bbox_to_docproto_bbox_empty_coordinate():
    docproto = documentai.Document(
        pages=[
            documentai.Document.Page(
                dimension=documentai.Document.Page.Dimension(width=2550, height=3300)
            )
        ]
    )
    with open("tests/unit/resources/converters/test_type_1.json", "r") as f:
        invoice = f.read()
    with open("tests/unit/resources/converters/test_config_type_1.json", "r") as f:
        config = f.read()
    b = Block.load_blocks_from_schema(
        input_data=invoice, input_config=config, base_docproto=docproto
    )
    b[0].bounding_box = []

    actual = bbox_conversion.convert_bbox_to_docproto_bbox(block=b[0])

    assert actual == documentai.BoundingPoly()


def test_convert_bbox_to_docproto_bbox_type_1():
    docproto = documentai.Document(
        pages=[
            documentai.Document.Page(
                dimension=documentai.Document.Page.Dimension(width=2550, height=3300)
            )
        ]
    )
    with open("tests/unit/resources/converters/test_type_1.json", "r") as f:
        invoice = f.read()
    with open("tests/unit/resources/converters/test_config_type_1.json", "r") as f:
        config = f.read()

    b = Block.load_blocks_from_schema(
        input_data=invoice, input_config=config, base_docproto=docproto
    )

    actual = bbox_conversion.convert_bbox_to_docproto_bbox(block=b[0])

    assert actual.normalized_vertices != []
    assert actual.vertices == []
    assert "x" in str(actual.normalized_vertices)
    assert "y" in str(actual.normalized_vertices)


def test_convert_bbox_to_docproto_bbox_type_2():
    docproto = documentai.Document(
        pages=[
            documentai.Document.Page(
                dimension=documentai.Document.Page.Dimension(width=2550, height=3300)
            )
        ]
    )
    with open("tests/unit/resources/converters/test_type_2.json", "r") as f:
        invoice = f.read()
    with open("tests/unit/resources/converters/test_config_type_2.json", "r") as f:
        config = f.read()
    b = Block.load_blocks_from_schema(
        input_data=invoice, input_config=config, base_docproto=docproto
    )

    actual = bbox_conversion.convert_bbox_to_docproto_bbox(block=b[0])

    assert actual.normalized_vertices != []
    assert actual.vertices == []
    assert "x" in str(actual.normalized_vertices)
    assert "y" in str(actual.normalized_vertices)


def test_convert_bbox_to_docproto_bbox_type_3():
    docproto = documentai.Document(
        pages=[
            documentai.Document.Page(
                dimension=documentai.Document.Page.Dimension(width=2550, height=3300)
            )
        ]
    )
    with open("tests/unit/resources/converters/test_type_3.json", "r") as f:
        invoice = f.read()
    with open("tests/unit/resources/converters/test_config_type_3.json", "r") as f:
        config = f.read()
    b = Block.load_blocks_from_schema(
        input_data=invoice, input_config=config, base_docproto=docproto
    )

    actual = bbox_conversion.convert_bbox_to_docproto_bbox(block=b[0])

    assert actual.normalized_vertices != []
    assert actual.vertices == []
    assert "x" in str(actual.normalized_vertices)
    assert "y" in str(actual.normalized_vertices)
