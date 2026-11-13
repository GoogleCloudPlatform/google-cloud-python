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

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.maps.routing.v2",
    manifest={
        "TollPass",
    },
)


class TollPass(proto.Enum):
    r"""List of toll passes around the world that we support.

    Values:
        TOLL_PASS_UNSPECIFIED (0):
            Not used. If this value is used, then the
            request fails.
        AU_ETOLL_TAG (82):
            Sydney toll pass. See additional details at
            https://www.myetoll.com.au.
        AU_EWAY_TAG (83):
            Sydney toll pass. See additional details at
            https://www.tollpay.com.au.
        AU_LINKT (2):
            Australia-wide toll pass.
            See additional details at
            https://www.linkt.com.au/.
        AR_TELEPASE (3):
            Argentina toll pass. See additional details
            at https://telepase.com.ar
        BR_AUTO_EXPRESO (81):
            Brazil toll pass. See additional details at
            https://www.autoexpreso.com
        BR_CONECTCAR (7):
            Brazil toll pass. See additional details at
            https://conectcar.com.
        BR_MOVE_MAIS (8):
            Brazil toll pass. See additional details at
            https://movemais.com.
        BR_PASSA_RAPIDO (88):
            Brazil toll pass. See additional details at
            https://pasorapido.gob.do/
        BR_SEM_PARAR (9):
            Brazil toll pass. See additional details at
            https://www.semparar.com.br.
        BR_TAGGY (10):
            Brazil toll pass. See additional details at
            https://taggy.com.br.
        BR_VELOE (11):
            Brazil toll pass. See additional details at
            https://veloe.com.br/site/onde-usar.
        CA_US_AKWASASNE_SEAWAY_CORPORATE_CARD (84):
            Canada to United States border crossing.
        CA_US_AKWASASNE_SEAWAY_TRANSIT_CARD (85):
            Canada to United States border crossing.
        CA_US_BLUE_WATER_EDGE_PASS (18):
            Ontario, Canada to Michigan, United States
            border crossing.
        CA_US_CONNEXION (19):
            Ontario, Canada to Michigan, United States
            border crossing.
        CA_US_NEXUS_CARD (20):
            Canada to United States border crossing.
        ID_E_TOLL (16):
            Indonesia.
            E-card provided by multiple banks used to pay
            for tolls. All e-cards via banks are charged the
            same so only one enum value is needed. E.g.
            - Bank Mandiri
              https://www.bankmandiri.co.id/e-money
            - BCA https://www.bca.co.id/flazz
            - BNI
              https://www.bni.co.id/id-id/ebanking/tapcash
        IN_FASTAG (78):
            India.
        IN_LOCAL_HP_PLATE_EXEMPT (79):
            India, HP state plate exemption.
        JP_ETC (98):
            Japan
            ETC. Electronic wireless system to collect
            tolls. https://www.go-etc.jp/
        JP_ETC2 (99):
            Japan
            ETC2.0. New version of ETC with further discount
            and bidirectional communication between devices
            on vehicles and antennas on the road.
            https://www.go-etc.jp/etc2/index.html
        MX_IAVE (90):
            Mexico toll pass.
            https://iave.capufe.gob.mx/#/
        MX_PASE (91):
            Mexico
            https://www.pase.com.mx
        MX_QUICKPASS (93):
            Mexico
            https://operadoravial.com/quick-pass/
        MX_SISTEMA_TELEPEAJE_CHIHUAHUA (89):
            http://appsh.chihuahua.gob.mx/transparencia/?doc=/ingresos/TelepeajeFormato4.pdf
        MX_TAG_IAVE (12):
            Mexico
        MX_TAG_TELEVIA (13):
            Mexico toll pass company. One of many
            operating in Mexico City. See additional details
            at https://www.televia.com.mx.
        MX_TELEVIA (92):
            Mexico toll pass company. One of many
            operating in Mexico City.
            https://www.televia.com.mx
        MX_VIAPASS (14):
            Mexico toll pass. See additional details at
            https://www.viapass.com.mx/viapass/web_home.aspx.
        US_AL_FREEDOM_PASS (21):
            AL, USA.
        US_AK_ANTON_ANDERSON_TUNNEL_BOOK_OF_10_TICKETS (22):
            AK, USA.
        US_CA_FASTRAK (4):
            CA, USA.
        US_CA_FASTRAK_CAV_STICKER (86):
            Indicates driver has any FasTrak pass in
            addition to the DMV issued Clean Air Vehicle
            (CAV) sticker.
            https://www.bayareafastrak.org/en/guide/doINeedFlex.shtml
        US_CO_EXPRESSTOLL (23):
            CO, USA.
        US_CO_GO_PASS (24):
            CO, USA.
        US_DE_EZPASSDE (25):
            DE, USA.
        US_FL_BOB_SIKES_TOLL_BRIDGE_PASS (65):
            FL, USA.
        US_FL_DUNES_COMMUNITY_DEVELOPMENT_DISTRICT_EXPRESSCARD (66):
            FL, USA.
        US_FL_EPASS (67):
            FL, USA.
        US_FL_GIBA_TOLL_PASS (68):
            FL, USA.
        US_FL_LEEWAY (69):
            FL, USA.
        US_FL_SUNPASS (70):
            FL, USA.
        US_FL_SUNPASS_PRO (71):
            FL, USA.
        US_IL_EZPASSIL (73):
            IL, USA.
        US_IL_IPASS (72):
            IL, USA.
        US_IN_EZPASSIN (26):
            IN, USA.
        US_KS_BESTPASS_HORIZON (27):
            KS, USA.
        US_KS_KTAG (28):
            KS, USA.
        US_KS_NATIONALPASS (29):
            KS, USA.
        US_KS_PREPASS_ELITEPASS (30):
            KS, USA.
        US_KY_RIVERLINK (31):
            KY, USA.
        US_LA_GEAUXPASS (32):
            LA, USA.
        US_LA_TOLL_TAG (33):
            LA, USA.
        US_MA_EZPASSMA (6):
            MA, USA.
        US_MD_EZPASSMD (34):
            MD, USA.
        US_ME_EZPASSME (35):
            ME, USA.
        US_MI_AMBASSADOR_BRIDGE_PREMIER_COMMUTER_CARD (36):
            MI, USA.
        US_MI_BCPASS (94):
            MI, USA.
        US_MI_BREAKAWAY (101):
            MI, USA.
        US_MI_GROSSE_ILE_TOLL_BRIDGE_PASS_TAG (37):
            MI, USA.
        US_MI_IQ_PROX_CARD (38):
            MI, USA.
            Deprecated as this pass type no longer exists.
        US_MI_IQ_TAG (95):
            MI, USA.
        US_MI_MACKINAC_BRIDGE_MAC_PASS (39):
            MI, USA.
        US_MI_NEXPRESS_TOLL (40):
            MI, USA.
        US_MN_EZPASSMN (41):
            MN, USA.
        US_NC_EZPASSNC (42):
            NC, USA.
        US_NC_PEACH_PASS (87):
            NC, USA.
        US_NC_QUICK_PASS (43):
            NC, USA.
        US_NH_EZPASSNH (80):
            NH, USA.
        US_NJ_DOWNBEACH_EXPRESS_PASS (75):
            NJ, USA.
        US_NJ_EZPASSNJ (74):
            NJ, USA.
        US_NY_EXPRESSPASS (76):
            NY, USA.
        US_NY_EZPASSNY (77):
            NY, USA.
        US_OH_EZPASSOH (44):
            OH, USA.
        US_PA_EZPASSPA (45):
            PA, USA.
        US_RI_EZPASSRI (46):
            RI, USA.
        US_SC_PALPASS (47):
            SC, USA.
        US_TX_AVI_TAG (97):
            TX, USA.
        US_TX_BANCPASS (48):
            TX, USA.
        US_TX_DEL_RIO_PASS (49):
            TX, USA.
        US_TX_EFAST_PASS (50):
            TX, USA.
        US_TX_EAGLE_PASS_EXPRESS_CARD (51):
            TX, USA.
        US_TX_EPTOLL (52):
            TX, USA.
        US_TX_EZ_CROSS (53):
            TX, USA.
        US_TX_EZTAG (54):
            TX, USA.
        US_TX_FUEGO_TAG (96):
            TX, USA.
        US_TX_LAREDO_TRADE_TAG (55):
            TX, USA.
        US_TX_PLUSPASS (56):
            TX, USA.
        US_TX_TOLLTAG (57):
            TX, USA.
        US_TX_TXTAG (58):
            TX, USA.
        US_TX_XPRESS_CARD (59):
            TX, USA.
        US_UT_ADAMS_AVE_PARKWAY_EXPRESSCARD (60):
            UT, USA.
        US_VA_EZPASSVA (61):
            VA, USA.
        US_WA_BREEZEBY (17):
            WA, USA.
        US_WA_GOOD_TO_GO (1):
            WA, USA.
        US_WV_EZPASSWV (62):
            WV, USA.
        US_WV_MEMORIAL_BRIDGE_TICKETS (63):
            WV, USA.
        US_WV_MOV_PASS (100):
            WV, USA
        US_WV_NEWELL_TOLL_BRIDGE_TICKET (64):
            WV, USA.
    """

    TOLL_PASS_UNSPECIFIED = 0
    AU_ETOLL_TAG = 82
    AU_EWAY_TAG = 83
    AU_LINKT = 2
    AR_TELEPASE = 3
    BR_AUTO_EXPRESO = 81
    BR_CONECTCAR = 7
    BR_MOVE_MAIS = 8
    BR_PASSA_RAPIDO = 88
    BR_SEM_PARAR = 9
    BR_TAGGY = 10
    BR_VELOE = 11
    CA_US_AKWASASNE_SEAWAY_CORPORATE_CARD = 84
    CA_US_AKWASASNE_SEAWAY_TRANSIT_CARD = 85
    CA_US_BLUE_WATER_EDGE_PASS = 18
    CA_US_CONNEXION = 19
    CA_US_NEXUS_CARD = 20
    ID_E_TOLL = 16
    IN_FASTAG = 78
    IN_LOCAL_HP_PLATE_EXEMPT = 79
    JP_ETC = 98
    JP_ETC2 = 99
    MX_IAVE = 90
    MX_PASE = 91
    MX_QUICKPASS = 93
    MX_SISTEMA_TELEPEAJE_CHIHUAHUA = 89
    MX_TAG_IAVE = 12
    MX_TAG_TELEVIA = 13
    MX_TELEVIA = 92
    MX_VIAPASS = 14
    US_AL_FREEDOM_PASS = 21
    US_AK_ANTON_ANDERSON_TUNNEL_BOOK_OF_10_TICKETS = 22
    US_CA_FASTRAK = 4
    US_CA_FASTRAK_CAV_STICKER = 86
    US_CO_EXPRESSTOLL = 23
    US_CO_GO_PASS = 24
    US_DE_EZPASSDE = 25
    US_FL_BOB_SIKES_TOLL_BRIDGE_PASS = 65
    US_FL_DUNES_COMMUNITY_DEVELOPMENT_DISTRICT_EXPRESSCARD = 66
    US_FL_EPASS = 67
    US_FL_GIBA_TOLL_PASS = 68
    US_FL_LEEWAY = 69
    US_FL_SUNPASS = 70
    US_FL_SUNPASS_PRO = 71
    US_IL_EZPASSIL = 73
    US_IL_IPASS = 72
    US_IN_EZPASSIN = 26
    US_KS_BESTPASS_HORIZON = 27
    US_KS_KTAG = 28
    US_KS_NATIONALPASS = 29
    US_KS_PREPASS_ELITEPASS = 30
    US_KY_RIVERLINK = 31
    US_LA_GEAUXPASS = 32
    US_LA_TOLL_TAG = 33
    US_MA_EZPASSMA = 6
    US_MD_EZPASSMD = 34
    US_ME_EZPASSME = 35
    US_MI_AMBASSADOR_BRIDGE_PREMIER_COMMUTER_CARD = 36
    US_MI_BCPASS = 94
    US_MI_BREAKAWAY = 101
    US_MI_GROSSE_ILE_TOLL_BRIDGE_PASS_TAG = 37
    US_MI_IQ_PROX_CARD = 38
    US_MI_IQ_TAG = 95
    US_MI_MACKINAC_BRIDGE_MAC_PASS = 39
    US_MI_NEXPRESS_TOLL = 40
    US_MN_EZPASSMN = 41
    US_NC_EZPASSNC = 42
    US_NC_PEACH_PASS = 87
    US_NC_QUICK_PASS = 43
    US_NH_EZPASSNH = 80
    US_NJ_DOWNBEACH_EXPRESS_PASS = 75
    US_NJ_EZPASSNJ = 74
    US_NY_EXPRESSPASS = 76
    US_NY_EZPASSNY = 77
    US_OH_EZPASSOH = 44
    US_PA_EZPASSPA = 45
    US_RI_EZPASSRI = 46
    US_SC_PALPASS = 47
    US_TX_AVI_TAG = 97
    US_TX_BANCPASS = 48
    US_TX_DEL_RIO_PASS = 49
    US_TX_EFAST_PASS = 50
    US_TX_EAGLE_PASS_EXPRESS_CARD = 51
    US_TX_EPTOLL = 52
    US_TX_EZ_CROSS = 53
    US_TX_EZTAG = 54
    US_TX_FUEGO_TAG = 96
    US_TX_LAREDO_TRADE_TAG = 55
    US_TX_PLUSPASS = 56
    US_TX_TOLLTAG = 57
    US_TX_TXTAG = 58
    US_TX_XPRESS_CARD = 59
    US_UT_ADAMS_AVE_PARKWAY_EXPRESSCARD = 60
    US_VA_EZPASSVA = 61
    US_WA_BREEZEBY = 17
    US_WA_GOOD_TO_GO = 1
    US_WV_EZPASSWV = 62
    US_WV_MEMORIAL_BRIDGE_TICKETS = 63
    US_WV_MOV_PASS = 100
    US_WV_NEWELL_TOLL_BRIDGE_TICKET = 64


__all__ = tuple(sorted(__protobuf__.manifest))
