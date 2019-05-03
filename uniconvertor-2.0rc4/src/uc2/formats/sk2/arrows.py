# -*- coding: utf-8 -*-
#
#  Copyright (C) 2018 by Igor E. Novikov
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from copy import deepcopy
from uc2 import libgeom, sk2const

ARROWS = [
    # arrow01
    [[[-0.0703358759842482, -0.500848400807721],
      [[-2.6254854822834606, -2.1585491882092955],
       [-2.0769815452755864, -3.004123991358902],
       [2.5525617618110275, -0.0005334401777999376],
       [-2.0769815452755864, 3.00050592990094],
       [-2.625202017716531, 2.1546476621844044],
       [-0.0714697342519647, 0.499214591318263],
       [-0.0703358759842482, -0.500848400807721]], 1]],
    # arrow07
    [[[-0.09146973425196472, 0.499214591318263],
      [[-2.645202017716531, 2.1546476621844044],
       [[-2.919562445962508, 2.3681165033198055],
        [-2.8928871851688496, 2.67961022568447],
        [-2.7400590682547263, 2.877906096009904], 0],
       [[-2.5987217871988073, 3.0612925024010944],
        [-2.337971502189297, 3.1220306896924863],
        [-2.0969815452755864, 3.00050592990094], 0], [2.5325617618110274, 0.0],
       [-2.0969815452755864, -3.00050592990094],
       [[-2.337971502189297, -3.1220306896924863],
        [-2.5987217871988073, -3.0612925024010944],
        [-2.7400590682547263, -2.877906096009904], 0],
       [[-2.8928871851688496, -2.67961022568447],
        [-2.919562445962508, -2.3681165033198055],
        [-2.645202017716531, -2.1546476621844044], 0],
       [-0.09146973425196472, -0.499214591318263],
       [-0.09146973425196472, 0.499214591318263]], 1]],
    # arrow02
    [[[-0.0544712837770458, -0.5009404628086858], [
        [[-0.12221931527310836, -1.3479325887929376],
         [-0.36174687432822683, -2.193507391942544],
         [-0.7724870318085415, -3.0249089667456937], 0],
        [6.283512968191458, -0.00090896674569374],
        [-0.7724870318085415, 3.023091033254306],
        [[-0.36174687432822683, 2.191405993884227],
         [-0.12193585070617985, 1.3463981198684793],
         [-0.0544712837770458, 0.4991225293172983], 0],
        [-0.0544712837770458, -0.5009404628086858]], 1]],
    # arrow03
    [[[-0.09937906003936359, -3.0863208661417656],
      [[6.071644562007879, 4.1338582643546395e-05],
       [-0.09937906003936359, 3.084419291338549]],
      [-0.09937906003936359, -3.0863208661417656], 1]],
    # arrow04
    [[[-0.11157717488167596, -2.422632750984286],
      [[3.128139360551395, -0.3204595226378294],
       [3.128139360551395, -2.4325540108268053],
       [4.136139360551394, -2.4325540108268053],
       [4.136139360551394, 2.43198142224406],
       [3.128139360551395, 2.43198142224406],
       [3.128139360551395, 0.33320976870075325],
       [-0.11157717488167596, 2.43198142224406],
       [-0.11157717488167596, -2.422632750984286]], 1]],
    # arrow05
    [[[-0.05728249100607674, -0.5011397637795565],
      [[-1.4890620185651315, -1.5111240157480603],
       [0.8413001861592775, -1.5111240157480603],
       [3.1716623908836867, 0.0008759842519394101],
       [0.8413001861592775, 1.5108917322834352],
       [-1.4890620185651315, 1.5108917322834352],
       [-0.05643209730528942, 0.49892322834642755],
       [-0.05728249100607674, -0.5011397637795565]], 1]],
    # arrow06
    [[[-0.08429220751522783, -1.7987741141732578],
      [[2.693660548390284, -1.7987741141732578],
       [5.469629052327291, 0.0015093503936712827],
       [2.693660548390284, 1.8017928149606002],
       [-0.08429220751522783, 1.8017928149606002],
       [-0.08429220751522783, -1.7987741141732578]], 1]],
    # arrow08
    [[[-0.05943686613304233, -0.5021546505905772],
      [[-1.2117203306999715, -2.2298711860236478],
       [1.0180119527645952, -0.7439499261811284],
       [0.278169433079556, -2.2298711860236478],
       [4.360626125992941, -0.002123154527585158],
       [0.278169433079556, 2.2276091289369813],
       [1.0180119527645952, 0.7416878690944619],
       [-1.2117203306999715, 2.2276091289369813],
       [-0.05915340156611337, 0.49790834153540686],
       [-0.05943686613304233, -0.5021546505905772]], 1]],
    # arrow09
    [[[-0.0784351600907005, -0.5005259596456426],
      [[-3.462718624657629, -2.3813133612204456],
       [4.897501847783315, -2.3813133612204456], [9.137281375342369, 0.0],
       [4.897501847783315, 2.3813133612204456],
       [-3.462718624657629, 2.3813133612204456],
       [-0.0784351600907005, 0.5005259596456426],
       [-0.0784351600907005, -0.5005259596456426]], 1]],
    # arrow10
    [[[-0.04061454172566137, -0.5002096864699492],
      [[3.3088027811089837, -2.380997088044752],
       [11.669023253549927, -2.380997088044752], [7.385023253549928, 0.0],
       [11.669023253549927, 2.380997088044752],
       [3.3088027811089837, 2.380997088044752],
       [-0.04061454172566137, 0.5002096864699492],
       [-0.04061454172566137, -0.5002096864699492]], 1]],
    # arrow11
    [[[4.199654542342855, -2.017906786638764],
      [[4.5559695029727765, -1.6615918260088427],
       [2.8962844636026976, -0.0019067866387639798],
       [4.5559695029727765, 1.6577782527313145],
       [3.8433395817129337, 2.370408173991157],
       [1.8273395817129343, 0.3544081739911572],
       [1.4710246210830131, -0.0019067866387639798],
       [1.8273395817129343, -0.3582217472686853],
       [3.8433395817129337, -2.374221747268685],
       [4.199654542342855, -2.017906786638764]], 1],
     [[-0.044943882853994574, -0.501938282701756],
      [[1.8273395817129343, -2.374221747268685],
       [2.1836545423428557, -2.017906786638764],
       [2.5399695029727765, -1.6615918260088427],
       [0.8802844636026983, -0.0019067866387639798],
       [2.5399695029727765, 1.6577782527313145],
       [1.8273395817129343, 2.370408173991157],
       [-0.044943882853994574, 0.49812470942422804],
       [-0.044943882853994574, -0.501938282701756]], 1]],
    # arrow12
    [[[1.1795827673691046, -2.0144564468504016],
      [[1.5358977279990258, -2.370771407480323],
       [3.551897727999026, -0.354771407480323],
       [3.9082126886289466, 0.001543553149598309],
       [3.551897727999026, 0.3578585137795195],
       [1.5358977279990258, 2.373858513779519],
       [0.8232678067391832, 1.6612285925196768],
       [2.482952846109262, 0.001543553149598309],
       [0.8232678067391832, -1.6581414862204804],
       [1.1795827673691046, -2.0144564468504016]], 1],
     [[-0.03307864995373018, -0.4984879429133937],
      [[-1.1927321932608164, -1.6581414862204804],
       [-0.8364172326308953, -2.0144564468504016],
       [-0.48010227200097405, -2.370771407480323],
       [1.5358977279990258, -0.354771407480323],
       [1.892212688628947, 0.001543553149598309],
       [1.5358977279990258, 0.3578585137795195],
       [-0.48010227200097405, 2.373858513779519],
       [-1.1927321932608164, 1.6612285925196768],
       [-0.03307864995373018, 0.5015750492125903],
       [-0.03307864995373018, -0.4984879429133937]], 1]],
    # arrow13
    [[[-0.07515305043639975, -0.49954601377954444],
      [[-0.8345546252395493, -2.0155145177165523],
       [0.6814138786974584, -2.0155145177165523],
       [1.6894138786974584, 0.00048548228344758027],
       [0.6814138786974584, 2.0164854822834473],
       [-0.8345546252395493, 2.014501230314943],
       [-0.07543651500332871, 0.5005169783464396],
       [-0.07515305043639975, -0.49954601377954444]], 1]],
    # arrow14
    [[[-0.07067755274660592, -0.49859793307087696],
      [[-1.5866460566836136, -2.014566437007885],
       [0.429353943316386, -2.014566437007885],
       [2.445353943316386, 0.0014335629921150561],
       [0.429353943316386, 2.0174335629921147],
       [-1.5866460566836136, 2.0174335629921147],
       [-0.07067755274660592, 0.5014650590551071],
       [-0.07067755274660592, -0.49859793307087696]], 1]],
    # arrow15
    [[[0.9030214003526889, 0.7856685531495942],
      [[2.9955568334235547, 0.0010386318897518398],
       [0.9030214003526889, -0.7835912893700907],
       [0.9030214003526889, 0.7856685531495942]], 1],
     [[-0.10497859964731115, -2.2383314468504056],
      [[5.866485967281823, 0.0010386318897518398],
       [-0.10497859964731115, 2.240408710629909],
       [-0.10497859964731115, -2.2383314468504056]], 1]],
    # arrow16
    [[[-0.11634774280553298, -2.0160194389763846],
      [[3.9156522571944663, -2.0160194389763846],
       [3.9156522571944663, 2.015980561023615],
       [-0.11634774280553298, 2.015980561023615],
       [-0.11634774280553298, -2.0160194389763846]], 1]],
    # arrow17
    [[[2.8, 0.0],
      [[[2.8, 0.8282869606299208], [2.1282869606299206, 1.5], [1.3, 1.5], 4],
       [[0.4717130393700789, 1.5], [-0.20000000000000004, 0.8282869606299208],
        [-0.20000000000000004, 0.0], 4],
       [[-0.20000000000000004, -0.828286960629921], [0.4717130393700789, -1.5],
        [1.3, -1.5], 4],
       [[2.1282869606299206, -1.5], [2.8, -0.828286960629921], [2.8, 0.0], 4]],
      1]],
    # arrow18
    [[[4.799479166666667, 0.0], [
        [[4.799479166666667, 1.3804782677165353], [3.679957434383202, 2.5],
         [2.2994791666666665, 2.5], 4],
        [[0.9837108177493441, 2.5], [-0.0949922801068324, 1.4829735434993232],
         [-0.1932296029673099, 0.19232115443252207], 4],
        [[-0.1980609467145465, 0.12884644677349888],
         [-0.20052083333333343, 0.06470991879921284],
         [-0.20052083333333343, 0.0], 4],
        [[-0.20052083333333343, -0.05931742556594477],
         [-0.1984538452717139, -0.1181530435637228],
         [-0.1943879823728028, -0.17643874076900534], 4],
        [[-0.10383012689705601, -1.474620178523026], [0.9783183245160765, -2.5],
         [2.2994791666666665, -2.5], 4],
        [[3.679957434383202, -2.5], [4.799479166666667, -1.380478267716535],
         [4.799479166666667, 0.0], 4]], 1]],
]

ARROWS_CACHE = []


def get_arrow_paths(arrow):
    if isinstance(arrow, int):
        if not arrow < len(ARROWS):
            arrow = 0
        return deepcopy(ARROWS[arrow])
    return arrow


def get_arrow_cpath(arrow, trafo=None):
    if trafo is None:
        trafo = sk2const.NORMAL_TRAFO
    if isinstance(arrow, int):
        if not ARROWS_CACHE:
            ARROWS_CACHE.extend([None, ] * len(ARROWS))
        if not arrow < len(ARROWS):
            arrow = 0
        if ARROWS_CACHE[arrow] is None:
            ARROWS_CACHE[arrow] = libgeom.create_cpath(ARROWS[arrow])
        return libgeom.apply_trafo(ARROWS_CACHE[arrow], trafo, True)
    ret = None
    if arrow and isinstance(arrow, list):
        try:
            ret = libgeom.create_cpath(arrow)
        except Exception:
            ret = None
    if ret:
        return libgeom.apply_trafo(ret, trafo, True)
    return ret
