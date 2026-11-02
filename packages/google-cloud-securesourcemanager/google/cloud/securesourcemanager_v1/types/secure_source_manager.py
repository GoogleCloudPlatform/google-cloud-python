# -*- coding: utf-8 -*-
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.securesourcemanager.v1",
    manifest={
        "Instance",
        "Repository",
        "Hook",
        "BranchRule",
        "PullRequest",
        "FileDiff",
        "Issue",
        "IssueComment",
        "PullRequestComment",
        "Ref",
        "ListInstancesRequest",
        "ListInstancesResponse",
        "GetInstanceRequest",
        "CreateInstanceRequest",
        "DeleteInstanceRequest",
        "OperationMetadata",
        "ListRepositoriesRequest",
        "ListRepositoriesResponse",
        "GetRepositoryRequest",
        "CreateRepositoryRequest",
        "UpdateRepositoryRequest",
        "DeleteRepositoryRequest",
        "ListHooksRequest",
        "ListHooksResponse",
        "GetHookRequest",
        "CreateHookRequest",
        "UpdateHookRequest",
        "DeleteHookRequest",
        "GetBranchRuleRequest",
        "CreateBranchRuleRequest",
        "ListBranchRulesRequest",
        "DeleteBranchRuleRequest",
        "UpdateBranchRuleRequest",
        "ListBranchRulesResponse",
        "CreatePullRequestRequest",
        "GetPullRequestRequest",
        "ListPullRequestsRequest",
        "ListPullRequestsResponse",
        "UpdatePullRequestRequest",
        "MergePullRequestRequest",
        "OpenPullRequestRequest",
        "ClosePullRequestRequest",
        "ListPullRequestFileDiffsRequest",
        "ListPullRequestFileDiffsResponse",
        "CreateIssueRequest",
        "GetIssueRequest",
        "ListIssuesRequest",
        "ListIssuesResponse",
        "UpdateIssueRequest",
        "DeleteIssueRequest",
        "CloseIssueRequest",
        "OpenIssueRequest",
        "TreeEntry",
        "FetchTreeRequest",
        "FetchTreeResponse",
        "FetchBlobRequest",
        "FetchBlobResponse",
        "FetchRefsRequest",
        "FetchRefsResponse",
        "ListPullRequestCommentsRequest",
        "ListPullRequestCommentsResponse",
        "CreatePullRequestCommentRequest",
        "BatchCreatePullRequestCommentsRequest",
        "BatchCreatePullRequestCommentsResponse",
        "UpdatePullRequestCommentRequest",
        "DeletePullRequestCommentRequest",
        "GetPullRequestCommentRequest",
        "ResolvePullRequestCommentsRequest",
        "ResolvePullRequestCommentsResponse",
        "UnresolvePullRequestCommentsRequest",
        "UnresolvePullRequestCommentsResponse",
        "CreateIssueCommentRequest",
        "GetIssueCommentRequest",
        "ListIssueCommentsRequest",
        "ListIssueCommentsResponse",
        "UpdateIssueCommentRequest",
        "DeleteIssueCommentRequest",
    },
)


class Instance(proto.Message):
    r"""A resource that represents a Secure Source Manager instance.

    Attributes:
        name (str):
            Identifier. A unique identifier for an instance. The name
            should be of the format:
            ``projects/{project_number}/locations/{location_id}/instances/{instance_id}``

            ``project_number``: Maps to a unique int64 id assigned to
            each project.

            ``location_id``: Refers to the region where the instance
            will be deployed. Since Secure Source Manager is a regional
            service, it must be one of the valid GCP regions.

            ``instance_id``: User provided name for the instance, must
            be unique for a project_number and location_id combination.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update timestamp.
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs. Keys and values can
            contain only lowercase letters, numeric characters,
            underscores, and dashes. For more information, see
            `Requirements for
            labels <https://cloud.google.com/resource-manager/docs/best-practices-labels#label_encoding>`__.
        private_config (google.cloud.securesourcemanager_v1.types.Instance.PrivateConfig):
            Optional. Private settings for private
            instance.
        state (google.cloud.securesourcemanager_v1.types.Instance.State):
            Output only. Current state of the instance.
        state_note (google.cloud.securesourcemanager_v1.types.Instance.StateNote):
            Output only. An optional field providing
            information about the current instance state.
        kms_key (str):
            Optional. Immutable. Customer-managed encryption key name,
            in the format
            projects/*/locations/*/keyRings/*/cryptoKeys/*.
        host_config (google.cloud.securesourcemanager_v1.types.Instance.HostConfig):
            Output only. A list of hostnames for this
            instance.
        workforce_identity_federation_config (google.cloud.securesourcemanager_v1.types.Instance.WorkforceIdentityFederationConfig):
            Optional. Configuration for Workforce
            Identity Federation to support third party
            identity provider. If unset, defaults to the
            Google OIDC IdP.
        satisfies_pzi (bool):
            Output only. Reserved for future use.
        satisfies_pzs (bool):
            Output only. Reserved for future use.
    """

    class State(proto.Enum):
        r"""Secure Source Manager instance state.

        Values:
            STATE_UNSPECIFIED (0):
                Not set. This should only be the case for
                incoming requests.
            CREATING (1):
                Instance is being created.
            ACTIVE (2):
                Instance is ready.
            DELETING (3):
                Instance is being deleted.
            PAUSED (4):
                Instance is paused.
            UNKNOWN (6):
                Instance is unknown, we are not sure if it's
                functioning.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3
        PAUSED = 4
        UNKNOWN = 6

    class StateNote(proto.Enum):
        r"""Provides information about the current instance state.

        Values:
            STATE_NOTE_UNSPECIFIED (0):
                STATE_NOTE_UNSPECIFIED as the first value of State.
            PAUSED_CMEK_UNAVAILABLE (1):
                CMEK access is unavailable.
            INSTANCE_RESUMING (2):
                INSTANCE_RESUMING indicates that the instance was previously
                paused and is under the process of being brought back.
        """

        STATE_NOTE_UNSPECIFIED = 0
        PAUSED_CMEK_UNAVAILABLE = 1
        INSTANCE_RESUMING = 2

    class HostConfig(proto.Message):
        r"""HostConfig has different instance endpoints.

        Attributes:
            html (str):
                Output only. HTML hostname.
            api (str):
                Output only. API hostname.
            git_http (str):
                Output only. Git HTTP hostname.
            git_ssh (str):
                Output only. Git SSH hostname.
        """

        html: str = proto.Field(
            proto.STRING,
            number=1,
        )
        api: str = proto.Field(
            proto.STRING,
            number=2,
        )
        git_http: str = proto.Field(
            proto.STRING,
            number=3,
        )
        git_ssh: str = proto.Field(
            proto.STRING,
            number=4,
        )

    class PrivateConfig(proto.Message):
        r"""PrivateConfig includes settings for private instance.

        Attributes:
            is_private (bool):
                Required. Immutable. Indicate if it's private
                instance.
            ca_pool (str):
                Optional. Immutable. CA pool resource, resource must in the
                format of
                ``projects/{project}/locations/{location}/caPools/{ca_pool}``.
            http_service_attachment (str):
                Output only. Service Attachment for HTTP, resource is in the
                format of
                ``projects/{project}/regions/{region}/serviceAttachments/{service_attachment}``.
            ssh_service_attachment (str):
                Output only. Service Attachment for SSH, resource is in the
                format of
                ``projects/{project}/regions/{region}/serviceAttachments/{service_attachment}``.
            psc_allowed_projects (MutableSequence[str]):
                Optional. Additional allowed projects for
                setting up PSC connections. Instance host
                project is automatically allowed and does not
                need to be included in this list.
            custom_host_config (google.cloud.securesourcemanager_v1.types.Instance.PrivateConfig.CustomHostConfig):
                Optional. Custom host config for the
                instance.
        """

        class CustomHostConfig(proto.Message):
            r"""Custom host config for the instance.

            Attributes:
                html (str):
                    Required. The custom UI hostname for the
                    instance, e.g.,
                    "git.source.internal.mycompany.com".
                api (str):
                    Required. The custom API hostname for the
                    instance, e.g.,
                    "api.source.internal.mycompany.com".
                git_ssh (str):
                    Required. The custom git ssh hostname for the
                    instance, e.g.,
                    "ssh.source.internal.mycompany.com".
                git_http (str):
                    Required. The custom git http hostname for
                    the instance, e.g.,
                    "git.source.internal.mycompany.com".
            """

            html: str = proto.Field(
                proto.STRING,
                number=1,
            )
            api: str = proto.Field(
                proto.STRING,
                number=2,
            )
            git_ssh: str = proto.Field(
                proto.STRING,
                number=3,
            )
            git_http: str = proto.Field(
                proto.STRING,
                number=4,
            )

        is_private: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        ca_pool: str = proto.Field(
            proto.STRING,
            number=2,
        )
        http_service_attachment: str = proto.Field(
            proto.STRING,
            number=3,
        )
        ssh_service_attachment: str = proto.Field(
            proto.STRING,
            number=4,
        )
        psc_allowed_projects: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=6,
        )
        custom_host_config: "Instance.PrivateConfig.CustomHostConfig" = proto.Field(
            proto.MESSAGE,
            number=7,
            message="Instance.PrivateConfig.CustomHostConfig",
        )

    class WorkforceIdentityFederationConfig(proto.Message):
        r"""WorkforceIdentityFederationConfig allows this instance to
        support users from external identity providers.

        Attributes:
            enabled (bool):
                Optional. Immutable. Whether Workforce
                Identity Federation is enabled.
        """

        enabled: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    private_config: PrivateConfig = proto.Field(
        proto.MESSAGE,
        number=13,
        message=PrivateConfig,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    state_note: StateNote = proto.Field(
        proto.ENUM,
        number=10,
        enum=StateNote,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=11,
    )
    host_config: HostConfig = proto.Field(
        proto.MESSAGE,
        number=9,
        message=HostConfig,
    )
    workforce_identity_federation_config: WorkforceIdentityFederationConfig = (
        proto.Field(
            proto.MESSAGE,
            number=14,
            message=WorkforceIdentityFederationConfig,
        )
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=18,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=19,
    )


class Repository(proto.Message):
    r"""Metadata of a Secure Source Manager repository.

    Attributes:
        name (str):
            Identifier. A unique identifier for a repository. The name
            should be of the format:
            ``projects/{project}/locations/{location_id}/repositories/{repository_id}``
        description (str):
            Optional. Description of the repository,
            which cannot exceed 500 characters.
        instance (str):
            Optional. The name of the instance in which the repository
            is hosted, formatted as
            ``projects/{project_number}/locations/{location_id}/instances/{instance_id}``
            When creating repository via
            securesourcemanager.googleapis.com, this field is used as
            input. When creating repository via \*.sourcemanager.dev,
            this field is output only.
        uid (str):
            Output only. Unique identifier of the
            repository.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update timestamp.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        uris (google.cloud.securesourcemanager_v1.types.Repository.URIs):
            Output only. URIs for the repository.
        initial_config (google.cloud.securesourcemanager_v1.types.Repository.InitialConfig):
            Input only. Initial configurations for the
            repository.
        service_account (str):
            Optional. Repository level service account
            (BYOSA).
        scan_config (google.cloud.securesourcemanager_v1.types.Repository.ScanConfig):
            Optional. Provides configuration for
            scanning.
    """

    class URIs(proto.Message):
        r"""URIs for the repository.

        Attributes:
            html (str):
                Output only. HTML is the URI for user to view
                the repository in a browser.
            git_https (str):
                Output only. git_https is the git HTTPS URI for git
                operations.
            api (str):
                Output only. API is the URI for API access.
        """

        html: str = proto.Field(
            proto.STRING,
            number=1,
        )
        git_https: str = proto.Field(
            proto.STRING,
            number=2,
        )
        api: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class InitialConfig(proto.Message):
        r"""Repository initialization configuration.

        Attributes:
            default_branch (str):
                Default branch name of the repository.
            gitignores (MutableSequence[str]):
                List of gitignore template names user can
                choose from. Valid values: actionscript, ada,
                agda, android, anjuta, ansible,
                appcelerator-titanium, app-engine, archives,
                arch-linux-packages, atmel-studio, autotools,
                backup, bazaar, bazel, bitrix, bricx-cc, c,
                cake-php, calabash, cf-wheels, chef-cookbook,
                clojure, cloud9, c-make, code-igniter, code-kit,
                code-sniffer, common-lisp, composer, concrete5,
                coq, cordova, cpp, craft-cms, cuda, cvs, d,
                dart, dart-editor, delphi, diff, dm,
                dreamweaver, dropbox, drupal, drupal-7, eagle,
                eclipse, eiffel-studio, elisp, elixir, elm,
                emacs, ensime, epi-server, erlang, esp-idf,
                espresso, exercism, expression-engine, ext-js,
                fancy, finale, flex-builder, force-dot-com,
                fortran, fuel-php, gcov, git-book,
                gnome-shell-extension, go, godot, gpg, gradle,
                grails, gwt, haskell, hugo, iar-ewarm, idris,
                igor-pro, images, infor-cms, java, jboss,
                jboss-4, jboss-6, jdeveloper, jekyll,
                jenkins-home, jenv, jet-brains, jigsaw, joomla,
                julia, jupyter-notebooks, kate, kdevelop4,
                kentico, ki-cad, kohana, kotlin, lab-view,
                laravel, lazarus, leiningen, lemon-stand,
                libre-office, lilypond, linux, lithium, logtalk,
                lua, lyx, mac-os, magento, magento-1, magento-2,
                matlab, maven, mercurial, mercury, metals,
                meta-programming-system, meteor,
                microsoft-office, model-sim, momentics,
                mono-develop, nanoc, net-beans, nikola, nim,
                ninja, node, notepad-pp, nwjs, objective--c,
                ocaml, octave, opa, open-cart, openssl,
                oracle-forms, otto, packer, patch, perl, perl6,
                phalcon, phoenix, pimcore, play-framework,
                plone, prestashop, processing, psoc-creator,
                puppet, pure-script, putty, python, qooxdoo, qt,
                r, racket, rails, raku, red, redcar, redis,
                rhodes-rhomobile, ros, ruby, rust, sam, sass,
                sbt, scala, scheme, scons, scrivener, sdcc,
                seam-gen, sketch-up, slick-edit, smalltalk,
                snap, splunk, stata, stella, sublime-text,
                sugar-crm, svn, swift, symfony, symphony-cms,
                synopsys-vcs, tags, terraform, tex, text-mate,
                textpattern, think-php, tortoise-git,
                turbo-gears-2, typo3, umbraco, unity,
                unreal-engine, vagrant, vim, virtual-env,
                virtuoso, visual-studio, visual-studio-code,
                vue, vvvv, waf, web-methods, windows,
                word-press, xcode, xilinx, xilinx-ise, xojo,
                yeoman, yii, zend-framework, zephir.
            license_ (str):
                License template name user can choose from.
                Valid values: license-0bsd,
                license-389-exception, aal, abstyles,
                adobe-2006, adobe-glyph, adsl, afl-1-1, afl-1-2,
                afl-2-0, afl-2-1, afl-3-0, afmparse, agpl-1-0,
                agpl-1-0-only, agpl-1-0-or-later, agpl-3-0-only,
                agpl-3-0-or-later, aladdin, amdplpa, aml, ampas,
                antlr-pd, antlr-pd-fallback, apache-1-0,
                apache-1-1, apache-2-0, apafml, apl-1-0,
                apsl-1-0, apsl-1-1, apsl-1-2, apsl-2-0,
                artistic-1-0, artistic-1-0-cl8,
                artistic-1-0-perl, artistic-2-0,
                autoconf-exception-2-0, autoconf-exception-3-0,
                bahyph, barr, beerware, bison-exception-2-2,
                bittorrent-1-0, bittorrent-1-1, blessing,
                blueoak-1-0-0, bootloader-exception, borceux,
                bsd-1-clause, bsd-2-clause,
                bsd-2-clause-freebsd, bsd-2-clause-netbsd,
                bsd-2-clause-patent, bsd-2-clause-views,
                bsd-3-clause, bsd-3-clause-attribution,
                bsd-3-clause-clear, bsd-3-clause-lbnl,
                bsd-3-clause-modification,
                bsd-3-clause-no-nuclear-license,
                bsd-3-clause-no-nuclear-license-2014,
                bsd-3-clause-no-nuclear-warranty,
                bsd-3-clause-open-mpi, bsd-4-clause,
                bsd-4-clause-shortened, bsd-4-clause-uc,
                bsd-protection, bsd-source-code, bsl-1-0,
                busl-1-1, cal-1-0,
                cal-1-0-combined-work-exception, caldera,
                catosl-1-1, cc0-1-0, cc-by-1-0, cc-by-2-0,
                cc-by-3-0, cc-by-3-0-at, cc-by-3-0-us,
                cc-by-4-0, cc-by-nc-1-0, cc-by-nc-2-0,
                cc-by-nc-3-0, cc-by-nc-4-0, cc-by-nc-nd-1-0,
                cc-by-nc-nd-2-0, cc-by-nc-nd-3-0,
                cc-by-nc-nd-3-0-igo, cc-by-nc-nd-4-0,
                cc-by-nc-sa-1-0, cc-by-nc-sa-2-0,
                cc-by-nc-sa-3-0, cc-by-nc-sa-4-0, cc-by-nd-1-0,
                cc-by-nd-2-0, cc-by-nd-3-0, cc-by-nd-4-0,
                cc-by-sa-1-0, cc-by-sa-2-0, cc-by-sa-2-0-uk,
                cc-by-sa-2-1-jp, cc-by-sa-3-0, cc-by-sa-3-0-at,
                cc-by-sa-4-0, cc-pddc, cddl-1-0, cddl-1-1,
                cdla-permissive-1-0, cdla-sharing-1-0,
                cecill-1-0, cecill-1-1, cecill-2-0, cecill-2-1,
                cecill-b, cecill-c, cern-ohl-1-1, cern-ohl-1-2,
                cern-ohl-p-2-0, cern-ohl-s-2-0, cern-ohl-w-2-0,
                clartistic, classpath-exception-2-0,
                clisp-exception-2-0, cnri-jython, cnri-python,
                cnri-python-gpl-compatible, condor-1-1,
                copyleft-next-0-3-0, copyleft-next-0-3-1,
                cpal-1-0, cpl-1-0, cpol-1-02, crossword,
                crystal-stacker, cua-opl-1-0, cube, c-uda-1-0,
                curl, d-fsl-1-0, diffmark,
                digirule-foss-exception, doc, dotseqn, drl-1-0,
                dsdp, dvipdfm, ecl-1-0, ecl-2-0,
                ecos-exception-2-0, efl-1-0, efl-2-0, egenix,
                entessa, epics, epl-1-0, epl-2-0, erlpl-1-1,
                etalab-2-0, eu-datagrid, eupl-1-0, eupl-1-1,
                eupl-1-2, eurosym, fair,
                fawkes-runtime-exception, fltk-exception,
                font-exception-2-0, frameworx-1-0, freebsd-doc,
                freeimage, freertos-exception-2-0, fsfap, fsful,
                fsfullr, ftl, gcc-exception-2-0,
                gcc-exception-3-1, gd, gfdl-1-1-invariants-only,
                gfdl-1-1-invariants-or-later,
                gfdl-1-1-no-invariants-only,
                gfdl-1-1-no-invariants-or-later, gfdl-1-1-only,
                gfdl-1-1-or-later, gfdl-1-2-invariants-only,
                gfdl-1-2-invariants-or-later,
                gfdl-1-2-no-invariants-only,
                gfdl-1-2-no-invariants-or-later, gfdl-1-2-only,
                gfdl-1-2-or-later, gfdl-1-3-invariants-only,
                gfdl-1-3-invariants-or-later,
                gfdl-1-3-no-invariants-only,
                gfdl-1-3-no-invariants-or-later, gfdl-1-3-only,
                gfdl-1-3-or-later, giftware, gl2ps, glide,
                glulxe, glwtpl, gnu-javamail-exception, gnuplot,
                gpl-1-0-only, gpl-1-0-or-later, gpl-2-0-only,
                gpl-2-0-or-later, gpl-3-0-linking-exception,
                gpl-3-0-linking-source-exception, gpl-3-0-only,
                gpl-3-0-or-later, gpl-cc-1-0, gsoap-1-3b,
                haskell-report, hippocratic-2-1, hpnd,
                hpnd-sell-variant, htmltidy,
                i2p-gpl-java-exception, ibm-pibs, icu, ijg,
                image-magick, imatix, imlib2, info-zip, intel,
                intel-acpi, interbase-1-0, ipa, ipl-1-0, isc,
                jasper-2-0, jpnic, json, lal-1-2, lal-1-3,
                latex2e, leptonica, lgpl-2-0-only,
                lgpl-2-0-or-later, lgpl-2-1-only,
                lgpl-2-1-or-later, lgpl-3-0-linking-exception,
                lgpl-3-0-only, lgpl-3-0-or-later, lgpllr,
                libpng, libpng-2-0, libselinux-1-0, libtiff,
                libtool-exception, liliq-p-1-1, liliq-r-1-1,
                liliq-rplus-1-1, linux-openib,
                linux-syscall-note, llvm-exception, lpl-1-0,
                lpl-1-02, lppl-1-0, lppl-1-1, lppl-1-2,
                lppl-1-3a, lppl-1-3c, lzma-exception,
                make-index, mif-exception, miros, mit, mit-0,
                mit-advertising, mit-cmu, mit-enna, mit-feh,
                mit-modern-variant, mitnfa, mit-open-group,
                motosoto, mpich2, mpl-1-0, mpl-1-1, mpl-2-0,
                mpl-2-0-no-copyleft-exception, ms-pl, ms-rl,
                mtll, mulanpsl-1-0, mulanpsl-2-0, multics, mup,
                naist-2003, nasa-1-3, naumen, nbpl-1-0,
                ncgl-uk-2-0, ncsa, netcdf, net-snmp, newsletr,
                ngpl, nist-pd, nist-pd-fallback, nlod-1-0, nlpl,
                nokia, nokia-qt-exception-1-1, nosl, noweb,
                npl-1-0, npl-1-1, nposl-3-0, nrl, ntp, ntp-0,
                ocaml-lgpl-linking-exception,
                occt-exception-1-0, occt-pl, oclc-2-0, odbl-1-0,
                odc-by-1-0, ofl-1-0, ofl-1-0-no-rfn,
                ofl-1-0-rfn, ofl-1-1, ofl-1-1-no-rfn,
                ofl-1-1-rfn, ogc-1-0, ogdl-taiwan-1-0,
                ogl-canada-2-0, ogl-uk-1-0, ogl-uk-2-0,
                ogl-uk-3-0, ogtsl, oldap-1-1, oldap-1-2,
                oldap-1-3, oldap-1-4, oldap-2-0, oldap-2-0-1,
                oldap-2-1, oldap-2-2, oldap-2-2-1, oldap-2-2-2,
                oldap-2-3, oldap-2-4, oldap-2-7, oml,
                openjdk-assembly-exception-1-0, openssl,
                openvpn-openssl-exception, opl-1-0, oset-pl-2-1,
                osl-1-0, osl-1-1, osl-2-0, osl-2-1, osl-3-0,
                o-uda-1-0, parity-6-0-0, parity-7-0-0, pddl-1-0,
                php-3-0, php-3-01, plexus,
                polyform-noncommercial-1-0-0,
                polyform-small-business-1-0-0, postgresql,
                psf-2-0, psfrag,
                ps-or-pdf-font-exception-20170817, psutils,
                python-2-0, qhull, qpl-1-0,
                qt-gpl-exception-1-0, qt-lgpl-exception-1-1,
                qwt-exception-1-0, rdisc, rhecos-1-1, rpl-1-1,
                rpsl-1-0, rsa-md, rscpl, ruby, saxpath, sax-pd,
                scea, sendmail, sendmail-8-23, sgi-b-1-0,
                sgi-b-1-1, sgi-b-2-0, shl-0-51, shl-2-0,
                shl-2-1, simpl-2-0, sissl, sissl-1-2, sleepycat,
                smlnj, smppl, snia, spencer-86, spencer-94,
                spencer-99, spl-1-0, ssh-openssh, ssh-short,
                sspl-1-0, sugarcrm-1-1-3, swift-exception, swl,
                tapr-ohl-1-0, tcl, tcp-wrappers, tmate,
                torque-1-1, tosl, tu-berlin-1-0, tu-berlin-2-0,
                u-boot-exception-2-0, ucl-1-0, unicode-dfs-2015,
                unicode-dfs-2016, unicode-tou,
                universal-foss-exception-1-0, unlicense,
                upl-1-0, vim, vostrom, vsl-1-0, w3c,
                w3c-19980720, w3c-20150513, watcom-1-0, wsuipa,
                wtfpl, wxwindows-exception-3-1, x11, xerox,
                xfree86-1-1, xinetd, xnet, xpp, xskat, ypl-1-0,
                ypl-1-1, zed, zend-2-0, zimbra-1-3, zimbra-1-4,
                zlib, zlib-acknowledgement, zpl-1-1, zpl-2-0,
                zpl-2-1.
            readme (str):
                README template name.
                Valid template name(s) are: default.
        """

        default_branch: str = proto.Field(
            proto.STRING,
            number=1,
        )
        gitignores: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        license_: str = proto.Field(
            proto.STRING,
            number=3,
        )
        readme: str = proto.Field(
            proto.STRING,
            number=4,
        )

    class ScanConfig(proto.Message):
        r"""Configuration for scanning.

        Attributes:
            secret_scan_config (google.cloud.securesourcemanager_v1.types.Repository.ScanConfig.SecretScanConfig):
                Optional. Configuration for secret scanning.
        """

        class SecretScanConfig(proto.Message):
            r"""Configuration for secret scanning.

            Attributes:
                enabled (bool):
                    Optional. Enables secret scanning for the
                    repository.
                inspect_template (str):
                    Optional. The DLP inspect template to use for
                    secret scanning.
            """

            enabled: bool = proto.Field(
                proto.BOOL,
                number=1,
            )
            inspect_template: str = proto.Field(
                proto.STRING,
                number=2,
            )

        secret_scan_config: "Repository.ScanConfig.SecretScanConfig" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Repository.ScanConfig.SecretScanConfig",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=3,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=8,
    )
    uris: URIs = proto.Field(
        proto.MESSAGE,
        number=9,
        message=URIs,
    )
    initial_config: InitialConfig = proto.Field(
        proto.MESSAGE,
        number=10,
        message=InitialConfig,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=11,
    )
    scan_config: ScanConfig = proto.Field(
        proto.MESSAGE,
        number=13,
        message=ScanConfig,
    )


class Hook(proto.Message):
    r"""Metadata of a Secure Source Manager Hook.

    Attributes:
        name (str):
            Identifier. A unique identifier for a Hook. The name should
            be of the format:
            ``projects/{project}/locations/{location_id}/repositories/{repository_id}/hooks/{hook_id}``
        target_uri (str):
            Required. The target URI to which the
            payloads will be delivered.
        disabled (bool):
            Optional. Determines if the hook disabled or
            not. Set to true to stop sending traffic.
        events (MutableSequence[google.cloud.securesourcemanager_v1.types.Hook.HookEventType]):
            Optional. The events that trigger hook on.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update timestamp.
        uid (str):
            Output only. Unique identifier of the hook.
        push_option (google.cloud.securesourcemanager_v1.types.Hook.PushOption):
            Optional. The trigger option for push events.
        sensitive_query_string (str):
            Optional. The sensitive query string to be
            appended to the target URI.
    """

    class HookEventType(proto.Enum):
        r"""

        Values:
            UNSPECIFIED (0):
                Unspecified.
            PUSH (1):
                Push events are triggered when pushing to the
                repository.
            PULL_REQUEST (2):
                Pull request events are triggered when a pull
                request is opened, closed, reopened, or edited.
            PULL_REQUEST_COMMENT (3):
                Triggers when a general comment is added,
                edited, or deleted on a pull request.
        """

        UNSPECIFIED = 0
        PUSH = 1
        PULL_REQUEST = 2
        PULL_REQUEST_COMMENT = 3

    class PushOption(proto.Message):
        r"""

        Attributes:
            branch_filter (str):
                Optional. Trigger hook for matching branches only. Specified
                as glob pattern. If empty or *, events for all branches are
                reported. Examples: main, {main,release*}. See
                https://pkg.go.dev/github.com/gobwas/glob documentation.
        """

        branch_filter: str = proto.Field(
            proto.STRING,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    events: MutableSequence[HookEventType] = proto.RepeatedField(
        proto.ENUM,
        number=4,
        enum=HookEventType,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=7,
    )
    push_option: PushOption = proto.Field(
        proto.MESSAGE,
        number=9,
        message=PushOption,
    )
    sensitive_query_string: str = proto.Field(
        proto.STRING,
        number=10,
    )


class BranchRule(proto.Message):
    r"""Metadata of a BranchRule. BranchRule is the protection rule
    to enforce pre-defined rules on designated branches within a
    repository.

    Attributes:
        name (str):
            Identifier. A unique identifier for a BranchRule. The name
            should be of the format:
            ``projects/{project}/locations/{location}/repositories/{repository}/branchRules/{branch_rule}``
        uid (str):
            Output only. Unique identifier of the
            repository.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update timestamp.
        annotations (MutableMapping[str, str]):
            Optional. User annotations. These attributes
            can only be set and used by the user. See
            https://google.aip.dev/128#annotations for more
            details such as format and size limitations.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        include_pattern (str):
            Optional. The pattern of the branch that can match to this
            BranchRule. Specified as regex. .\* for all branches.
            Examples: main, (main|release.\*). Current MVP phase only
            support ``.*`` for wildcard.
        disabled (bool):
            Optional. Determines if the branch rule is
            disabled or not.
        require_pull_request (bool):
            Optional. Determines if the branch rule
            requires a pull request or not.
        minimum_reviews_count (int):
            Optional. The minimum number of reviews
            required for the branch rule to be matched.
        minimum_approvals_count (int):
            Optional. The minimum number of approvals
            required for the branch rule to be matched.
        require_code_owner_approval (bool):
            Optional. Determines if code owners must
            approve before merging to the branch.
        require_comments_resolved (bool):
            Optional. Determines if require comments
            resolved before merging to the branch.
        allow_stale_reviews (bool):
            Optional. Determines if allow stale reviews
            or approvals before merging to the branch.
        require_linear_history (bool):
            Optional. Determines if require linear
            history before merging to the branch.
        required_status_checks (MutableSequence[google.cloud.securesourcemanager_v1.types.BranchRule.Check]):
            Optional. List of required status checks
            before merging to the branch.
    """

    class Check(proto.Message):
        r"""Check is a type for status check.

        Attributes:
            context (str):
                Required. The context of the check.
        """

        context: str = proto.Field(
            proto.STRING,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=6,
    )
    include_pattern: str = proto.Field(
        proto.STRING,
        number=7,
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    require_pull_request: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    minimum_reviews_count: int = proto.Field(
        proto.INT32,
        number=10,
    )
    minimum_approvals_count: int = proto.Field(
        proto.INT32,
        number=11,
    )
    require_code_owner_approval: bool = proto.Field(
        proto.BOOL,
        number=16,
    )
    require_comments_resolved: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    allow_stale_reviews: bool = proto.Field(
        proto.BOOL,
        number=15,
    )
    require_linear_history: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    required_status_checks: MutableSequence[Check] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message=Check,
    )


class PullRequest(proto.Message):
    r"""Metadata of a PullRequest. PullRequest is the request
    from a user to merge a branch (head) into another branch (base).

    Attributes:
        name (str):
            Output only. Identifier. A unique identifier for a
            PullRequest. The number appended at the end is generated by
            the server. Format:
            ``projects/{project}/locations/{location}/repositories/{repository}/pullRequests/{pull_request_id}``
        title (str):
            Required. The pull request title.
        body (str):
            Optional. The pull request body. Provides a
            detailed description of the changes.
        base (google.cloud.securesourcemanager_v1.types.PullRequest.Branch):
            Required. The branch to merge changes in.
        head (google.cloud.securesourcemanager_v1.types.PullRequest.Branch):
            Immutable. The branch containing the changes
            to be merged.
        state (google.cloud.securesourcemanager_v1.types.PullRequest.State):
            Output only. State of the pull request (open,
            closed or merged).
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last updated timestamp.
        close_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Close timestamp (if closed or
            merged). Cleared when pull request is re-opened.
    """

    class State(proto.Enum):
        r"""State of the pull request.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified.
            OPEN (1):
                An open pull request.
            CLOSED (2):
                A closed pull request.
            MERGED (3):
                A merged pull request.
        """

        STATE_UNSPECIFIED = 0
        OPEN = 1
        CLOSED = 2
        MERGED = 3

    class Branch(proto.Message):
        r"""Branch represents a branch involved in a pull request.

        Attributes:
            ref (str):
                Required. Name of the branch.
            sha (str):
                Output only. The commit at the tip of the
                branch.
        """

        ref: str = proto.Field(
            proto.STRING,
            number=1,
        )
        sha: str = proto.Field(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: str = proto.Field(
        proto.STRING,
        number=3,
    )
    base: Branch = proto.Field(
        proto.MESSAGE,
        number=4,
        message=Branch,
    )
    head: Branch = proto.Field(
        proto.MESSAGE,
        number=5,
        message=Branch,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    close_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )


class FileDiff(proto.Message):
    r"""Metadata of a FileDiff. FileDiff represents a single file
    diff in a pull request.

    Attributes:
        name (str):
            Output only. The name of the file.
        action (google.cloud.securesourcemanager_v1.types.FileDiff.Action):
            Output only. The action taken on the file
            (eg. added, modified, deleted).
        sha (str):
            Output only. The commit pointing to the file
            changes.
        patch (str):
            Output only. The git patch containing the
            file changes.
    """

    class Action(proto.Enum):
        r"""Action taken on the file.

        Values:
            ACTION_UNSPECIFIED (0):
                Unspecified.
            ADDED (1):
                The file was added.
            MODIFIED (2):
                The file was modified.
            DELETED (3):
                The file was deleted.
        """

        ACTION_UNSPECIFIED = 0
        ADDED = 1
        MODIFIED = 2
        DELETED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    action: Action = proto.Field(
        proto.ENUM,
        number=2,
        enum=Action,
    )
    sha: str = proto.Field(
        proto.STRING,
        number=3,
    )
    patch: str = proto.Field(
        proto.STRING,
        number=4,
    )


class Issue(proto.Message):
    r"""Metadata of an Issue.

    Attributes:
        name (str):
            Identifier. Unique identifier for an issue. The issue id is
            generated by the server. Format:
            ``projects/{project}/locations/{location}/repositories/{repository}/issues/{issue_id}``
        title (str):
            Required. Issue title.
        body (str):
            Optional. Issue body. Provides a detailed
            description of the issue.
        state (google.cloud.securesourcemanager_v1.types.Issue.State):
            Output only. State of the issue.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last updated timestamp.
        close_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Close timestamp (if closed).
            Cleared when is re-opened.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
    """

    class State(proto.Enum):
        r"""Possible states of an issue.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified.
            OPEN (1):
                An open issue.
            CLOSED (2):
                A closed issue.
        """

        STATE_UNSPECIFIED = 0
        OPEN = 1
        CLOSED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    close_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=8,
    )


class IssueComment(proto.Message):
    r"""IssueComment represents a comment on an issue.

    Attributes:
        name (str):
            Identifier. Unique identifier for an issue comment. The
            comment id is generated by the server. Format:
            ``projects/{project}/locations/{location}/repositories/{repository}/issues/{issue}/issueComments/{comment_id}``
        body (str):
            Required. The comment body.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last updated timestamp.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    body: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class PullRequestComment(proto.Message):
    r"""PullRequestComment represents a comment on a pull request.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Unique identifier for the pull request comment.
            The comment id is generated by the server. Format:
            ``projects/{project}/locations/{location}/repositories/{repository}/pullRequests/{pull_request}/pullRequestComments/{comment_id}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last updated timestamp.
        review (google.cloud.securesourcemanager_v1.types.PullRequestComment.Review):
            Optional. The review summary comment.

            This field is a member of `oneof`_ ``comment_detail``.
        comment (google.cloud.securesourcemanager_v1.types.PullRequestComment.Comment):
            Optional. The general pull request comment.

            This field is a member of `oneof`_ ``comment_detail``.
        code (google.cloud.securesourcemanager_v1.types.PullRequestComment.Code):
            Optional. The comment on a code line.

            This field is a member of `oneof`_ ``comment_detail``.
    """

    class Review(proto.Message):
        r"""The review summary comment.

        Attributes:
            action_type (google.cloud.securesourcemanager_v1.types.PullRequestComment.Review.ActionType):
                Required. The review action type.
            body (str):
                Optional. The comment body.
            effective_commit_sha (str):
                Output only. The effective commit sha this
                review is pointing to.
        """

        class ActionType(proto.Enum):
            r"""The review action type.

            Values:
                ACTION_TYPE_UNSPECIFIED (0):
                    Unspecified.
                COMMENT (1):
                    A general review comment.
                CHANGE_REQUESTED (2):
                    Change required from this review.
                APPROVED (3):
                    Change approved from this review.
            """

            ACTION_TYPE_UNSPECIFIED = 0
            COMMENT = 1
            CHANGE_REQUESTED = 2
            APPROVED = 3

        action_type: "PullRequestComment.Review.ActionType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="PullRequestComment.Review.ActionType",
        )
        body: str = proto.Field(
            proto.STRING,
            number=2,
        )
        effective_commit_sha: str = proto.Field(
            proto.STRING,
            number=4,
        )

    class Comment(proto.Message):
        r"""The general pull request comment.

        Attributes:
            body (str):
                Required. The comment body.
        """

        body: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class Code(proto.Message):
        r"""The comment on a code line.

        Attributes:
            body (str):
                Required. The comment body.
            reply (str):
                Optional. Input only. The PullRequestComment
                resource name that this comment is replying to.
            position (google.cloud.securesourcemanager_v1.types.PullRequestComment.Position):
                Optional. The position of the comment.
            effective_root_comment (str):
                Output only. The root comment of the
                conversation, derived from the reply field.
            resolved (bool):
                Output only. Boolean indicator if the comment
                is resolved.
            effective_commit_sha (str):
                Output only. The effective commit sha this
                code comment is pointing to.
        """

        body: str = proto.Field(
            proto.STRING,
            number=1,
        )
        reply: str = proto.Field(
            proto.STRING,
            number=2,
        )
        position: "PullRequestComment.Position" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="PullRequestComment.Position",
        )
        effective_root_comment: str = proto.Field(
            proto.STRING,
            number=4,
        )
        resolved: bool = proto.Field(
            proto.BOOL,
            number=5,
        )
        effective_commit_sha: str = proto.Field(
            proto.STRING,
            number=7,
        )

    class Position(proto.Message):
        r"""The position of the code comment.

        Attributes:
            path (str):
                Required. The path of the file.
            line (int):
                Required. The line number of the comment.
                Positive value means it's on the new side of the
                diff, negative value means it's on the old side.
        """

        path: str = proto.Field(
            proto.STRING,
            number=1,
        )
        line: int = proto.Field(
            proto.INT64,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    review: Review = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="comment_detail",
        message=Review,
    )
    comment: Comment = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="comment_detail",
        message=Comment,
    )
    code: Code = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="comment_detail",
        message=Code,
    )


class Ref(proto.Message):
    r"""Ref represents a git reference within a repository.

    Attributes:
        name (str):
            Identifier. Name of the git reference (e.g.,
            'refs/heads/foo' or 'refs/tags/v1.0').
        target (str):
            Output only. The target of the reference,
            which is a commit SHA.
        type_ (google.cloud.securesourcemanager_v1.types.Ref.RefType):
            Output only. The type of the reference.
    """

    class RefType(proto.Enum):
        r"""The derived type of the reference (e.g., branch or tag) from
        the name.

        Values:
            REF_TYPE_UNSPECIFIED (0):
                Unspecified ref type.
            REF_TYPE_BRANCH (1):
                Represents a branch.
            REF_TYPE_TAG (2):
                Represents a tag.
        """

        REF_TYPE_UNSPECIFIED = 0
        REF_TYPE_BRANCH = 1
        REF_TYPE_TAG = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: RefType = proto.Field(
        proto.ENUM,
        number=3,
        enum=RefType,
    )


class ListInstancesRequest(proto.Message):
    r"""ListInstancesRequest is the request to list instances.

    Attributes:
        parent (str):
            Required. Parent value for
            ListInstancesRequest.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filter for filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListInstancesResponse(proto.Message):
    r"""

    Attributes:
        instances (MutableSequence[google.cloud.securesourcemanager_v1.types.Instance]):
            The list of instances.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    instances: MutableSequence["Instance"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Instance",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetInstanceRequest(proto.Message):
    r"""GetInstanceRequest is the request for getting an instance.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInstanceRequest(proto.Message):
    r"""CreateInstanceRequest is the request for creating an
    instance.

    Attributes:
        parent (str):
            Required. Value for parent.
        instance_id (str):
            Required. ID of the instance to be created.
        instance (google.cloud.securesourcemanager_v1.types.Instance):
            Required. The resource being created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance: "Instance" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Instance",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteInstanceRequest(proto.Message):
    r"""DeleteInstanceRequest is the request for deleting an
    instance.

    Attributes:
        name (str):
            Required. Name of the resource.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        force (bool):
            Optional. If set to true, will force the
            deletion of the instance.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have
            [Operation.error][google.longrunning.Operation.error] value
            with a [google.rpc.Status.code][google.rpc.Status.code] of
            1, corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class ListRepositoriesRequest(proto.Message):
    r"""ListRepositoriesRequest is request to list repositories.

    Attributes:
        parent (str):
            Required. Parent value for
            ListRepositoriesRequest.
        page_size (int):
            Optional. Requested page size. If
            unspecified, a default size of 30 will be used.
            The maximum value is 100; values above 100 will
            be coerced to 100.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filter results.
        instance (str):
            Optional. The name of the instance in which the repository
            is hosted, formatted as
            ``projects/{project_number}/locations/{location_id}/instances/{instance_id}``.
            When listing repositories via
            securesourcemanager.googleapis.com, this field is required.
            When listing repositories via \*.sourcemanager.dev, this
            field is ignored.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListRepositoriesResponse(proto.Message):
    r"""

    Attributes:
        repositories (MutableSequence[google.cloud.securesourcemanager_v1.types.Repository]):
            The list of repositories.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    repositories: MutableSequence["Repository"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Repository",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetRepositoryRequest(proto.Message):
    r"""GetRepositoryRequest is the request for getting a repository.

    Attributes:
        name (str):
            Required. Name of the repository to retrieve. The format is
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateRepositoryRequest(proto.Message):
    r"""CreateRepositoryRequest is the request for creating a
    repository.

    Attributes:
        parent (str):
            Required. The project in which to create the repository.
            Values are of the form
            ``projects/{project_number}/locations/{location_id}``
        repository (google.cloud.securesourcemanager_v1.types.Repository):
            Required. The resource being created.
        repository_id (str):
            Required. The ID to use for the repository, which will
            become the final component of the repository's resource
            name. This value should be 4-63 characters, and valid
            characters are /[a-z][0-9]-/.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    repository: "Repository" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Repository",
    )
    repository_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateRepositoryRequest(proto.Message):
    r"""UpdateRepositoryRequest is the request to update a
    repository.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the repository resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        repository (google.cloud.securesourcemanager_v1.types.Repository):
            Required. The repository being updated.
        validate_only (bool):
            Optional. False by default. If set to true,
            the request is validated and the user is
            provided with an expected result, but no actual
            change is made.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    repository: "Repository" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Repository",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DeleteRepositoryRequest(proto.Message):
    r"""DeleteRepositoryRequest is the request to delete a
    repository.

    Attributes:
        name (str):
            Required. Name of the repository to delete. The format is
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}``.
        allow_missing (bool):
            Optional. If set to true, and the repository
            is not found, the request will succeed but no
            action will be taken on the server.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ListHooksRequest(proto.Message):
    r"""ListHooksRequest is request to list hooks.

    Attributes:
        parent (str):
            Required. Parent value for ListHooksRequest.
        page_size (int):
            Optional. Requested page size. If
            unspecified, a default size of 30 will be used.
            The maximum value is 100; values above 100 will
            be coerced to 100.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListHooksResponse(proto.Message):
    r"""ListHooksResponse is response to list hooks.

    Attributes:
        hooks (MutableSequence[google.cloud.securesourcemanager_v1.types.Hook]):
            The list of hooks.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    hooks: MutableSequence["Hook"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Hook",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetHookRequest(proto.Message):
    r"""GetHookRequest is the request for getting a hook.

    Attributes:
        name (str):
            Required. Name of the hook to retrieve. The format is
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/hooks/{hook_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateHookRequest(proto.Message):
    r"""CreateHookRequest is the request for creating a hook.

    Attributes:
        parent (str):
            Required. The repository in which to create the hook. Values
            are of the form
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}``
        hook (google.cloud.securesourcemanager_v1.types.Hook):
            Required. The resource being created.
        hook_id (str):
            Required. The ID to use for the hook, which
            will become the final component of the hook's
            resource name. This value restricts to
            lower-case letters, numbers, and hyphen, with
            the first character a letter, the last a letter
            or a number, and a 63 character maximum.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    hook: "Hook" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Hook",
    )
    hook_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateHookRequest(proto.Message):
    r"""UpdateHookRequest is the request to update a hook.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the hook resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. The special value "\*" means full replacement.
        hook (google.cloud.securesourcemanager_v1.types.Hook):
            Required. The hook being updated.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    hook: "Hook" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Hook",
    )


class DeleteHookRequest(proto.Message):
    r"""DeleteHookRequest is the request to delete a hook.

    Attributes:
        name (str):
            Required. Name of the hook to delete. The format is
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/hooks/{hook_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetBranchRuleRequest(proto.Message):
    r"""GetBranchRuleRequest is the request for getting a branch
    rule.

    Attributes:
        name (str):
            Required. Name of the repository to retrieve. The format is
            ``projects/{project}/locations/{location}/repositories/{repository}/branchRules/{branch_rule}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateBranchRuleRequest(proto.Message):
    r"""CreateBranchRuleRequest is the request to create a branch
    rule.

    Attributes:
        parent (str):

        branch_rule (google.cloud.securesourcemanager_v1.types.BranchRule):

        branch_rule_id (str):

    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    branch_rule: "BranchRule" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="BranchRule",
    )
    branch_rule_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListBranchRulesRequest(proto.Message):
    r"""ListBranchRulesRequest is the request to list branch rules.

    Attributes:
        parent (str):

        page_size (int):
            Optional. Requested page size. If
            unspecified, a default size of 30 will be used.
            The maximum value is 100; values above 100 will
            be coerced to 100.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteBranchRuleRequest(proto.Message):
    r"""DeleteBranchRuleRequest is the request to delete a branch
    rule.

    Attributes:
        name (str):

        allow_missing (bool):
            Optional. If set to true, and the branch rule
            is not found, the request will succeed but no
            action will be taken on the server.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class UpdateBranchRuleRequest(proto.Message):
    r"""UpdateBranchRuleRequest is the request to update a
    branchRule.

    Attributes:
        branch_rule (google.cloud.securesourcemanager_v1.types.BranchRule):

        validate_only (bool):
            Optional. If set, validate the request and
            preview the review, but do not actually post it.
            (https://google.aip.dev/163, for declarative
            friendly)
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the branchRule resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. The special value "\*" means full
            replacement.
    """

    branch_rule: "BranchRule" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="BranchRule",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class ListBranchRulesResponse(proto.Message):
    r"""ListBranchRulesResponse is the response to listing
    branchRules.

    Attributes:
        branch_rules (MutableSequence[google.cloud.securesourcemanager_v1.types.BranchRule]):
            The list of branch rules.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    branch_rules: MutableSequence["BranchRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BranchRule",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreatePullRequestRequest(proto.Message):
    r"""CreatePullRequestRequest is the request to create a pull
    request.

    Attributes:
        parent (str):
            Required. The repository that the pull request is created
            from. Format:
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}``
        pull_request (google.cloud.securesourcemanager_v1.types.PullRequest):
            Required. The pull request to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    pull_request: "PullRequest" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PullRequest",
    )


class GetPullRequestRequest(proto.Message):
    r"""GetPullRequestRequest is the request to get a pull request.

    Attributes:
        name (str):
            Required. Name of the pull request to retrieve. The format
            is
            ``projects/{project}/locations/{location}/repositories/{repository}/pullRequests/{pull_request}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListPullRequestsRequest(proto.Message):
    r"""ListPullRequestsRequest is the request to list pull requests.

    Attributes:
        parent (str):
            Required. The repository in which to list pull requests.
            Format:
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}``
        page_size (int):
            Optional. Requested page size. If
            unspecified, a default size of 30 will be used.
            The maximum value is 100; values above 100 will
            be coerced to 100.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListPullRequestsResponse(proto.Message):
    r"""ListPullRequestsResponse is the response to list pull
    requests.

    Attributes:
        pull_requests (MutableSequence[google.cloud.securesourcemanager_v1.types.PullRequest]):
            The list of pull requests.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    pull_requests: MutableSequence["PullRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PullRequest",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdatePullRequestRequest(proto.Message):
    r"""UpdatePullRequestRequest is the request to update a pull
    request.

    Attributes:
        pull_request (google.cloud.securesourcemanager_v1.types.PullRequest):
            Required. The pull request to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the pull request resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. The special value "\*" means full
            replacement.
    """

    pull_request: "PullRequest" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PullRequest",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class MergePullRequestRequest(proto.Message):
    r"""MergePullRequestRequest is the request to merge a pull
    request.

    Attributes:
        name (str):
            Required. The pull request to merge. Format:
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/pullRequests/{pull_request_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OpenPullRequestRequest(proto.Message):
    r"""OpenPullRequestRequest is the request to open a pull request.

    Attributes:
        name (str):
            Required. The pull request to open. Format:
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/pullRequests/{pull_request_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ClosePullRequestRequest(proto.Message):
    r"""ClosePullRequestRequest is the request to close a pull
    request.

    Attributes:
        name (str):
            Required. The pull request to close. Format:
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/pullRequests/{pull_request_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListPullRequestFileDiffsRequest(proto.Message):
    r"""ListPullRequestFileDiffsRequest is the request to list pull
    request file diffs.

    Attributes:
        name (str):
            Required. The pull request to list file diffs for. Format:
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/pullRequests/{pull_request_id}``
        page_size (int):
            Optional. Requested page size. If
            unspecified, a default size of 30 will be used.
            The maximum value is 100; values above 100 will
            be coerced to 100.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListPullRequestFileDiffsResponse(proto.Message):
    r"""ListPullRequestFileDiffsResponse is the response containing
    file diffs returned from ListPullRequestFileDiffs.

    Attributes:
        file_diffs (MutableSequence[google.cloud.securesourcemanager_v1.types.FileDiff]):
            The list of pull request file diffs.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    file_diffs: MutableSequence["FileDiff"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FileDiff",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateIssueRequest(proto.Message):
    r"""The request to create an issue.

    Attributes:
        parent (str):
            Required. The repository in which to create the issue.
            Format:
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}``
        issue (google.cloud.securesourcemanager_v1.types.Issue):
            Required. The issue to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    issue: "Issue" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Issue",
    )


class GetIssueRequest(proto.Message):
    r"""The request to get an issue.

    Attributes:
        name (str):
            Required. Name of the issue to retrieve. The format is
            ``projects/{project}/locations/{location}/repositories/{repository}/issues/{issue_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListIssuesRequest(proto.Message):
    r"""The request to list issues.

    Attributes:
        parent (str):
            Required. The repository in which to list issues. Format:
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}``
        page_size (int):
            Optional. Requested page size. If
            unspecified, a default size of 30 will be used.
            The maximum value is 100; values above 100 will
            be coerced to 100.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Used to filter the resulting issues
            list.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListIssuesResponse(proto.Message):
    r"""The response to list issues.

    Attributes:
        issues (MutableSequence[google.cloud.securesourcemanager_v1.types.Issue]):
            The list of issues.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    issues: MutableSequence["Issue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Issue",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateIssueRequest(proto.Message):
    r"""The request to update an issue.

    Attributes:
        issue (google.cloud.securesourcemanager_v1.types.Issue):
            Required. The issue to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the issue resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. The special value "\*" means full replacement.
    """

    issue: "Issue" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Issue",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteIssueRequest(proto.Message):
    r"""The request to delete an issue.

    Attributes:
        name (str):
            Required. Name of the issue to delete. The format is
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/issues/{issue_id}``.
        etag (str):
            Optional. The current etag of the issue.
            If the etag is provided and does not match the
            current etag of the issue, deletion will be
            blocked and an ABORTED error will be returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CloseIssueRequest(proto.Message):
    r"""The request to close an issue.

    Attributes:
        name (str):
            Required. Name of the issue to close. The format is
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/issues/{issue_id}``.
        etag (str):
            Optional. The current etag of the issue.
            If the etag is provided and does not match the
            current etag of the issue, closing will be
            blocked and an ABORTED error will be returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OpenIssueRequest(proto.Message):
    r"""The request to open an issue.

    Attributes:
        name (str):
            Required. Name of the issue to open. The format is
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/issues/{issue_id}``.
        etag (str):
            Optional. The current etag of the issue.
            If the etag is provided and does not match the
            current etag of the issue, opening will be
            blocked and an ABORTED error will be returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TreeEntry(proto.Message):
    r"""Represents an entry within a tree structure (like a Git
    tree).

    Attributes:
        type_ (google.cloud.securesourcemanager_v1.types.TreeEntry.ObjectType):
            Output only. The type of the object (TREE,
            BLOB, COMMIT).  Output-only.
        sha (str):
            Output only. The SHA-1 hash of the object
            (unique identifier). Output-only.
        path (str):
            Output only. The path of the file or
            directory within the tree (e.g.,
            "src/main/java/MyClass.java"). Output-only.
        mode (str):
            Output only. The file mode as a string (e.g.,
            "100644"). Indicates file type. Output-only.
        size (int):
            Output only. The size of the object in bytes
            (only for blobs). Output-only.
    """

    class ObjectType(proto.Enum):
        r"""Defines the type of object the TreeEntry represents.

        Values:
            OBJECT_TYPE_UNSPECIFIED (0):
                Default value, indicating the object type is
                unspecified.
            TREE (1):
                Represents a directory (folder).
            BLOB (2):
                Represents a file (contains file data).
            COMMIT (3):
                Represents a pointer to another repository
                (submodule).
        """

        OBJECT_TYPE_UNSPECIFIED = 0
        TREE = 1
        BLOB = 2
        COMMIT = 3

    type_: ObjectType = proto.Field(
        proto.ENUM,
        number=1,
        enum=ObjectType,
    )
    sha: str = proto.Field(
        proto.STRING,
        number=2,
    )
    path: str = proto.Field(
        proto.STRING,
        number=3,
    )
    mode: str = proto.Field(
        proto.STRING,
        number=4,
    )
    size: int = proto.Field(
        proto.INT64,
        number=5,
    )


class FetchTreeRequest(proto.Message):
    r"""Request message for fetching a tree structure from a
    repository.

    Attributes:
        repository (str):
            Required. The format is
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}``.
            Specifies the repository to fetch the tree from.
        ref (str):
            Optional. ``ref`` can be a SHA-1 hash, a branch name, or a
            tag. Specifies which tree to fetch. If not specified, the
            default branch will be used.
        recursive (bool):
            Optional. If true, include all subfolders and
            their files in the response. If false, only the
            immediate children are returned.
        page_size (int):
            Optional. Requested page size.  Server may
            return fewer items than requested. If
            unspecified, at most 10,000 items will be
            returned.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
    """

    repository: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ref: str = proto.Field(
        proto.STRING,
        number=2,
    )
    recursive: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class FetchTreeResponse(proto.Message):
    r"""Response message containing a list of TreeEntry objects.

    Attributes:
        tree_entries (MutableSequence[google.cloud.securesourcemanager_v1.types.TreeEntry]):
            The list of TreeEntry objects.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    tree_entries: MutableSequence["TreeEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TreeEntry",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FetchBlobRequest(proto.Message):
    r"""Request message for fetching a blob (file content) from a
    repository.

    Attributes:
        repository (str):
            Required. The format is
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}``.
            Specifies the repository containing the blob.
        sha (str):
            Required. The SHA-1 hash of the blob to
            retrieve.
    """

    repository: str = proto.Field(
        proto.STRING,
        number=1,
    )
    sha: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FetchBlobResponse(proto.Message):
    r"""Response message containing the content of a blob.

    Attributes:
        sha (str):
            The SHA-1 hash of the blob.
        content (str):
            The content of the blob, encoded as base64.
    """

    sha: str = proto.Field(
        proto.STRING,
        number=1,
    )
    content: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FetchRefsRequest(proto.Message):
    r"""Request message for fetching git references from a
    repository.

    Attributes:
        repository (str):
            Required. The format is
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}``.
            Specifies the repository to fetch the references from.
        type_ (google.cloud.securesourcemanager_v1.types.Ref.RefType):
            Optional. The type of reference to fetch (eg.
            branch, tag). By default, all references are
            returned.
        page_size (int):
            Optional. Requested page size. If
            unspecified, a default size of 30 will be used.
            The maximum value is 100; values above 100 will
            be coerced to 100.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
    """

    repository: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: "Ref.RefType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="Ref.RefType",
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class FetchRefsResponse(proto.Message):
    r"""Response message containing a list of git references.

    Attributes:
        refs (MutableSequence[google.cloud.securesourcemanager_v1.types.Ref]):
            The list of git references.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    refs: MutableSequence["Ref"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Ref",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListPullRequestCommentsRequest(proto.Message):
    r"""The request to list pull request comments.

    Attributes:
        parent (str):
            Required. The pull request in which to list pull request
            comments. Format:
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/pullRequests/{pull_request_id}``
        page_size (int):
            Optional. Requested page size. If
            unspecified, a default size of 30 will be used.
            The maximum value is 100; values above 100 will
            be coerced to 100.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListPullRequestCommentsResponse(proto.Message):
    r"""The response to list pull request comments.

    Attributes:
        pull_request_comments (MutableSequence[google.cloud.securesourcemanager_v1.types.PullRequestComment]):
            The list of pull request comments.
        next_page_token (str):
            A token to set as page_token to retrieve the next page. If
            this field is omitted, there are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    pull_request_comments: MutableSequence["PullRequestComment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PullRequestComment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreatePullRequestCommentRequest(proto.Message):
    r"""The request to create a pull request comment.

    Attributes:
        parent (str):
            Required. The pull request in which to create the pull
            request comment. Format:
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/pullRequests/{pull_request_id}``
        pull_request_comment (google.cloud.securesourcemanager_v1.types.PullRequestComment):
            Required. The pull request comment to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    pull_request_comment: "PullRequestComment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PullRequestComment",
    )


class BatchCreatePullRequestCommentsRequest(proto.Message):
    r"""The request to batch create pull request comments.

    Attributes:
        parent (str):
            Required. The pull request in which to create the pull
            request comments. Format:
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/pullRequests/{pull_request_id}``
        requests (MutableSequence[google.cloud.securesourcemanager_v1.types.CreatePullRequestCommentRequest]):
            Required. The request message specifying the
            resources to create. There should be exactly one
            CreatePullRequestCommentRequest with
            CommentDetail being REVIEW in the list, and no
            more than 100 CreatePullRequestCommentRequests
            with CommentDetail being CODE in the list
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreatePullRequestCommentRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreatePullRequestCommentRequest",
    )


class BatchCreatePullRequestCommentsResponse(proto.Message):
    r"""The response to batch create pull request comments.

    Attributes:
        pull_request_comments (MutableSequence[google.cloud.securesourcemanager_v1.types.PullRequestComment]):
            The list of pull request comments created.
    """

    pull_request_comments: MutableSequence["PullRequestComment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PullRequestComment",
    )


class UpdatePullRequestCommentRequest(proto.Message):
    r"""The request to update a pull request comment.

    Attributes:
        pull_request_comment (google.cloud.securesourcemanager_v1.types.PullRequestComment):
            Required. The pull request comment to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the pull request comment resource by the
            update. Updatable fields are ``body``.
    """

    pull_request_comment: "PullRequestComment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PullRequestComment",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeletePullRequestCommentRequest(proto.Message):
    r"""The request to delete a pull request comment. A Review
    PullRequestComment cannot be deleted.

    Attributes:
        name (str):
            Required. Name of the pull request comment to delete. The
            format is
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/pullRequests/{pull_request_id}/pullRequestComments/{comment_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetPullRequestCommentRequest(proto.Message):
    r"""The request to get a pull request comment.

    Attributes:
        name (str):
            Required. Name of the pull request comment to retrieve. The
            format is
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/pullRequests/{pull_request_id}/pullRequestComments/{comment_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ResolvePullRequestCommentsRequest(proto.Message):
    r"""The request to resolve multiple pull request comments.

    Attributes:
        parent (str):
            Required. The pull request in which to resolve the pull
            request comments. Format:
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/pullRequests/{pull_request_id}``
        names (MutableSequence[str]):
            Required. The names of the pull request comments to resolve.
            Format:
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/pullRequests/{pull_request_id}/pullRequestComments/{comment_id}``
            Only comments from the same threads are allowed in the same
            request.
        auto_fill (bool):
            Optional. If set, at least one comment in a
            thread is required, rest of the comments in the
            same thread will be automatically updated to
            resolved. If unset, all comments in the same
            thread need be present.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    auto_fill: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ResolvePullRequestCommentsResponse(proto.Message):
    r"""The response to resolve multiple pull request comments.

    Attributes:
        pull_request_comments (MutableSequence[google.cloud.securesourcemanager_v1.types.PullRequestComment]):
            The list of pull request comments resolved.
    """

    pull_request_comments: MutableSequence["PullRequestComment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PullRequestComment",
    )


class UnresolvePullRequestCommentsRequest(proto.Message):
    r"""The request to unresolve multiple pull request comments.

    Attributes:
        parent (str):
            Required. The pull request in which to resolve the pull
            request comments. Format:
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/pullRequests/{pull_request_id}``
        names (MutableSequence[str]):
            Required. The names of the pull request comments to
            unresolve. Format:
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/pullRequests/{pull_request_id}/pullRequestComments/{comment_id}``
            Only comments from the same threads are allowed in the same
            request.
        auto_fill (bool):
            Optional. If set, at least one comment in a
            thread is required, rest of the comments in the
            same thread will be automatically updated to
            unresolved. If unset, all comments in the same
            thread need be present.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    auto_fill: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class UnresolvePullRequestCommentsResponse(proto.Message):
    r"""The response to unresolve multiple pull request comments.

    Attributes:
        pull_request_comments (MutableSequence[google.cloud.securesourcemanager_v1.types.PullRequestComment]):
            The list of pull request comments unresolved.
    """

    pull_request_comments: MutableSequence["PullRequestComment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PullRequestComment",
    )


class CreateIssueCommentRequest(proto.Message):
    r"""The request to create an issue comment.

    Attributes:
        parent (str):
            Required. The issue in which to create the issue comment.
            Format:
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/issues/{issue_id}``
        issue_comment (google.cloud.securesourcemanager_v1.types.IssueComment):
            Required. The issue comment to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    issue_comment: "IssueComment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="IssueComment",
    )


class GetIssueCommentRequest(proto.Message):
    r"""The request to get an issue comment.

    Attributes:
        name (str):
            Required. Name of the issue comment to retrieve. The format
            is
            ``projects/{project}/locations/{location}/repositories/{repository}/issues/{issue_id}/issueComments/{comment_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListIssueCommentsRequest(proto.Message):
    r"""The request to list issue comments.

    Attributes:
        parent (str):
            Required. The issue in which to list the comments. Format:
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/issues/{issue_id}``
        page_size (int):
            Optional. Requested page size. If
            unspecified, a default size of 30 will be used.
            The maximum value is 100; values above 100 will
            be coerced to 100.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListIssueCommentsResponse(proto.Message):
    r"""The response to list issue comments.

    Attributes:
        issue_comments (MutableSequence[google.cloud.securesourcemanager_v1.types.IssueComment]):
            The list of issue comments.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    issue_comments: MutableSequence["IssueComment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="IssueComment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateIssueCommentRequest(proto.Message):
    r"""The request to update an issue comment.

    Attributes:
        issue_comment (google.cloud.securesourcemanager_v1.types.IssueComment):
            Required. The issue comment to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the issue comment resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. The special value "\*" means full
            replacement.
    """

    issue_comment: "IssueComment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="IssueComment",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteIssueCommentRequest(proto.Message):
    r"""The request to delete an issue comment.

    Attributes:
        name (str):
            Required. Name of the issue comment to delete. The format is
            ``projects/{project_number}/locations/{location_id}/repositories/{repository_id}/issues/{issue_id}/issueComments/{comment_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
