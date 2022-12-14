<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use Exception;
use stdClass;
use SwaggerScarecrowLib\ApiHelper;

/**
 * Id issuing state
 */
class IssuingStateEnum
{
    public const USA_AL = 'USA_AL';

    public const USA_AK = 'USA_AK';

    public const USA_AZ = 'USA_AZ';

    public const USA_AR = 'USA_AR';

    public const USA_CA = 'USA_CA';

    public const USA_CO = 'USA_CO';

    public const USA_CT = 'USA_CT';

    public const USA_DE = 'USA_DE';

    public const USA_DC = 'USA_DC';

    public const USA_FL = 'USA_FL';

    public const USA_GA = 'USA_GA';

    public const USA_HI = 'USA_HI';

    public const USA_ID = 'USA_ID';

    public const USA_IL = 'USA_IL';

    public const USA_IN = 'USA_IN';

    public const USA_IA = 'USA_IA';

    public const USA_KS = 'USA_KS';

    public const USA_KY = 'USA_KY';

    public const USA_LA = 'USA_LA';

    public const USA_ME = 'USA_ME';

    public const USA_MD = 'USA_MD';

    public const USA_MA = 'USA_MA';

    public const USA_MI = 'USA_MI';

    public const USA_MN = 'USA_MN';

    public const USA_MS = 'USA_MS';

    public const USA_MO = 'USA_MO';

    public const USA_MT = 'USA_MT';

    public const USA_NE = 'USA_NE';

    public const USA_NV = 'USA_NV';

    public const USA_NH = 'USA_NH';

    public const USA_NJ = 'USA_NJ';

    public const USA_NM = 'USA_NM';

    public const USA_NY = 'USA_NY';

    public const USA_NC = 'USA_NC';

    public const USA_ND = 'USA_ND';

    public const USA_OH = 'USA_OH';

    public const USA_OK = 'USA_OK';

    public const USA_OR = 'USA_OR';

    public const USA_PA = 'USA_PA';

    public const USA_RI = 'USA_RI';

    public const USA_SC = 'USA_SC';

    public const USA_SD = 'USA_SD';

    public const USA_TN = 'USA_TN';

    public const USA_TX = 'USA_TX';

    public const USA_UT = 'USA_UT';

    public const USA_VT = 'USA_VT';

    public const USA_VA = 'USA_VA';

    public const USA_WA = 'USA_WA';

    public const USA_WV = 'USA_WV';

    public const USA_WI = 'USA_WI';

    public const USA_WY = 'USA_WY';

    public const MEX_AG = 'MEX_AG';

    public const MEX_BC = 'MEX_BC';

    public const MEX_BS = 'MEX_BS';

    public const MEX_CH = 'MEX_CH';

    public const MEX_CL = 'MEX_CL';

    public const MEX_CM = 'MEX_CM';

    public const MEX_CO = 'MEX_CO';

    public const MEX_CS = 'MEX_CS';

    public const MEX_DF = 'MEX_DF';

    public const MEX_DG = 'MEX_DG';

    public const MEX_GR = 'MEX_GR';

    public const MEX_GT = 'MEX_GT';

    public const MEX_HG = 'MEX_HG';

    public const MEX_JA = 'MEX_JA';

    public const MEX_ME = 'MEX_ME';

    public const MEX_MI = 'MEX_MI';

    public const MEX_MO = 'MEX_MO';

    public const MEX_NA = 'MEX_NA';

    public const MEX_NL = 'MEX_NL';

    public const MEX_OA = 'MEX_OA';

    public const MEX_PB = 'MEX_PB';

    public const MEX_QE = 'MEX_QE';

    public const MEX_QR = 'MEX_QR';

    public const MEX_SI = 'MEX_SI';

    public const MEX_SL = 'MEX_SL';

    public const MEX_SO = 'MEX_SO';

    public const MEX_TB = 'MEX_TB';

    public const MEX_TL = 'MEX_TL';

    public const MEX_TM = 'MEX_TM';

    public const MEX_VE = 'MEX_VE';

    public const MEX_YU = 'MEX_YU';

    public const MEX_ZA = 'MEX_ZA';

    public const CAN_AB = 'CAN_AB';

    public const CAN_BC = 'CAN_BC';

    public const CAN_MB = 'CAN_MB';

    public const CAN_NB = 'CAN_NB';

    public const CAN_NL = 'CAN_NL';

    public const CAN_NS = 'CAN_NS';

    public const CAN_NT = 'CAN_NT';

    public const CAN_NU = 'CAN_NU';

    public const CAN_ON = 'CAN_ON';

    public const CAN_PE = 'CAN_PE';

    public const CAN_QC = 'CAN_QC';

    public const CAN_SK = 'CAN_SK';

    public const CAN_YT = 'CAN_YT';

    public const ITA_AG = 'ITA_AG';

    public const ITA_AL = 'ITA_AL';

    public const ITA_AN = 'ITA_AN';

    public const ITA_AO = 'ITA_AO';

    public const ITA_AR = 'ITA_AR';

    public const ITA_AP = 'ITA_AP';

    public const ITA_AT = 'ITA_AT';

    public const ITA_AV = 'ITA_AV';

    public const ITA_BA = 'ITA_BA';

    public const ITA_BL = 'ITA_BL';

    public const ITA_BN = 'ITA_BN';

    public const ITA_BG = 'ITA_BG';

    public const ITA_BI = 'ITA_BI';

    public const ITA_BO = 'ITA_BO';

    public const ITA_BZ = 'ITA_BZ';

    public const ITA_BS = 'ITA_BS';

    public const ITA_BR = 'ITA_BR';

    public const ITA_CA = 'ITA_CA';

    public const ITA_CL = 'ITA_CL';

    public const ITA_CB = 'ITA_CB';

    public const ITA_CE = 'ITA_CE';

    public const ITA_CT = 'ITA_CT';

    public const ITA_CZ = 'ITA_CZ';

    public const ITA_CH = 'ITA_CH';

    public const ITA_CO = 'ITA_CO';

    public const ITA_CS = 'ITA_CS';

    public const ITA_CR = 'ITA_CR';

    public const ITA_KR = 'ITA_KR';

    public const ITA_CN = 'ITA_CN';

    public const ITA_EN = 'ITA_EN';

    public const ITA_FE = 'ITA_FE';

    public const ITA_FI = 'ITA_FI';

    public const ITA_FG = 'ITA_FG';

    public const ITA_FC = 'ITA_FC';

    public const ITA_FO = 'ITA_FO';

    public const ITA_FR = 'ITA_FR';

    public const ITA_GE = 'ITA_GE';

    public const ITA_GO = 'ITA_GO';

    public const ITA_GR = 'ITA_GR';

    public const ITA_IM = 'ITA_IM';

    public const ITA_IS = 'ITA_IS';

    public const ITA_SP = 'ITA_SP';

    public const ITA_AQ = 'ITA_AQ';

    public const ITA_LT = 'ITA_LT';

    public const ITA_LE = 'ITA_LE';

    public const ITA_LC = 'ITA_LC';

    public const ITA_LI = 'ITA_LI';

    public const ITA_LO = 'ITA_LO';

    public const ITA_LU = 'ITA_LU';

    public const ITA_MC = 'ITA_MC';

    public const ITA_MN = 'ITA_MN';

    public const ITA_MS = 'ITA_MS';

    public const ITA_MT = 'ITA_MT';

    public const ITA_ME = 'ITA_ME';

    public const ITA_MI = 'ITA_MI';

    public const ITA_MO = 'ITA_MO';

    public const ITA_NA = 'ITA_NA';

    public const ITA_NO = 'ITA_NO';

    public const ITA_NU = 'ITA_NU';

    public const ITA_OR = 'ITA_OR';

    public const ITA_PD = 'ITA_PD';

    public const ITA_PA = 'ITA_PA';

    public const ITA_PR = 'ITA_PR';

    public const ITA_PV = 'ITA_PV';

    public const ITA_PG = 'ITA_PG';

    public const ITA_PS = 'ITA_PS';

    public const ITA_PU = 'ITA_PU';

    public const ITA_PE = 'ITA_PE';

    public const ITA_PC = 'ITA_PC';

    public const ITA_PI = 'ITA_PI';

    public const ITA_PT = 'ITA_PT';

    public const ITA_PN = 'ITA_PN';

    public const ITA_PZ = 'ITA_PZ';

    public const ITA_PO = 'ITA_PO';

    public const ITA_RG = 'ITA_RG';

    public const ITA_RA = 'ITA_RA';

    public const ITA_RC = 'ITA_RC';

    public const ITA_RE = 'ITA_RE';

    public const ITA_RI = 'ITA_RI';

    public const ITA_RN = 'ITA_RN';

    public const ITA_RM = 'ITA_RM';

    public const ITA_RO = 'ITA_RO';

    public const ITA_SA = 'ITA_SA';

    public const ITA_SM = 'ITA_SM';

    public const ITA_SS = 'ITA_SS';

    public const ITA_SV = 'ITA_SV';

    public const ITA_SI = 'ITA_SI';

    public const ITA_SR = 'ITA_SR';

    public const ITA_SO = 'ITA_SO';

    public const ITA_TA = 'ITA_TA';

    public const ITA_TE = 'ITA_TE';

    public const ITA_TR = 'ITA_TR';

    public const ITA_TO = 'ITA_TO';

    public const ITA_TP = 'ITA_TP';

    public const ITA_TN = 'ITA_TN';

    public const ITA_TV = 'ITA_TV';

    public const ITA_TS = 'ITA_TS';

    public const ITA_UD = 'ITA_UD';

    public const ITA_VA = 'ITA_VA';

    public const ITA_VE = 'ITA_VE';

    public const ITA_VB = 'ITA_VB';

    public const ITA_VC = 'ITA_VC';

    public const ITA_VR = 'ITA_VR';

    public const ITA_VV = 'ITA_VV';

    public const ITA_VI = 'ITA_VI';

    public const ITA_VT = 'ITA_VT';

    public const ITA_OT = 'ITA_OT';

    private const _ALL_VALUES = [
        self::USA_AL,
        self::USA_AK,
        self::USA_AZ,
        self::USA_AR,
        self::USA_CA,
        self::USA_CO,
        self::USA_CT,
        self::USA_DE,
        self::USA_DC,
        self::USA_FL,
        self::USA_GA,
        self::USA_HI,
        self::USA_ID,
        self::USA_IL,
        self::USA_IN,
        self::USA_IA,
        self::USA_KS,
        self::USA_KY,
        self::USA_LA,
        self::USA_ME,
        self::USA_MD,
        self::USA_MA,
        self::USA_MI,
        self::USA_MN,
        self::USA_MS,
        self::USA_MO,
        self::USA_MT,
        self::USA_NE,
        self::USA_NV,
        self::USA_NH,
        self::USA_NJ,
        self::USA_NM,
        self::USA_NY,
        self::USA_NC,
        self::USA_ND,
        self::USA_OH,
        self::USA_OK,
        self::USA_OR,
        self::USA_PA,
        self::USA_RI,
        self::USA_SC,
        self::USA_SD,
        self::USA_TN,
        self::USA_TX,
        self::USA_UT,
        self::USA_VT,
        self::USA_VA,
        self::USA_WA,
        self::USA_WV,
        self::USA_WI,
        self::USA_WY,
        self::MEX_AG,
        self::MEX_BC,
        self::MEX_BS,
        self::MEX_CH,
        self::MEX_CL,
        self::MEX_CM,
        self::MEX_CO,
        self::MEX_CS,
        self::MEX_DF,
        self::MEX_DG,
        self::MEX_GR,
        self::MEX_GT,
        self::MEX_HG,
        self::MEX_JA,
        self::MEX_ME,
        self::MEX_MI,
        self::MEX_MO,
        self::MEX_NA,
        self::MEX_NL,
        self::MEX_OA,
        self::MEX_PB,
        self::MEX_QE,
        self::MEX_QR,
        self::MEX_SI,
        self::MEX_SL,
        self::MEX_SO,
        self::MEX_TB,
        self::MEX_TL,
        self::MEX_TM,
        self::MEX_VE,
        self::MEX_YU,
        self::MEX_ZA,
        self::CAN_AB,
        self::CAN_BC,
        self::CAN_MB,
        self::CAN_NB,
        self::CAN_NL,
        self::CAN_NS,
        self::CAN_NT,
        self::CAN_NU,
        self::CAN_ON,
        self::CAN_PE,
        self::CAN_QC,
        self::CAN_SK,
        self::CAN_YT,
        self::ITA_AG,
        self::ITA_AL,
        self::ITA_AN,
        self::ITA_AO,
        self::ITA_AR,
        self::ITA_AP,
        self::ITA_AT,
        self::ITA_AV,
        self::ITA_BA,
        self::ITA_BL,
        self::ITA_BN,
        self::ITA_BG,
        self::ITA_BI,
        self::ITA_BO,
        self::ITA_BZ,
        self::ITA_BS,
        self::ITA_BR,
        self::ITA_CA,
        self::ITA_CL,
        self::ITA_CB,
        self::ITA_CE,
        self::ITA_CT,
        self::ITA_CZ,
        self::ITA_CH,
        self::ITA_CO,
        self::ITA_CS,
        self::ITA_CR,
        self::ITA_KR,
        self::ITA_CN,
        self::ITA_EN,
        self::ITA_FE,
        self::ITA_FI,
        self::ITA_FG,
        self::ITA_FC,
        self::ITA_FO,
        self::ITA_FR,
        self::ITA_GE,
        self::ITA_GO,
        self::ITA_GR,
        self::ITA_IM,
        self::ITA_IS,
        self::ITA_SP,
        self::ITA_AQ,
        self::ITA_LT,
        self::ITA_LE,
        self::ITA_LC,
        self::ITA_LI,
        self::ITA_LO,
        self::ITA_LU,
        self::ITA_MC,
        self::ITA_MN,
        self::ITA_MS,
        self::ITA_MT,
        self::ITA_ME,
        self::ITA_MI,
        self::ITA_MO,
        self::ITA_NA,
        self::ITA_NO,
        self::ITA_NU,
        self::ITA_OR,
        self::ITA_PD,
        self::ITA_PA,
        self::ITA_PR,
        self::ITA_PV,
        self::ITA_PG,
        self::ITA_PS,
        self::ITA_PU,
        self::ITA_PE,
        self::ITA_PC,
        self::ITA_PI,
        self::ITA_PT,
        self::ITA_PN,
        self::ITA_PZ,
        self::ITA_PO,
        self::ITA_RG,
        self::ITA_RA,
        self::ITA_RC,
        self::ITA_RE,
        self::ITA_RI,
        self::ITA_RN,
        self::ITA_RM,
        self::ITA_RO,
        self::ITA_SA,
        self::ITA_SM,
        self::ITA_SS,
        self::ITA_SV,
        self::ITA_SI,
        self::ITA_SR,
        self::ITA_SO,
        self::ITA_TA,
        self::ITA_TE,
        self::ITA_TR,
        self::ITA_TO,
        self::ITA_TP,
        self::ITA_TN,
        self::ITA_TV,
        self::ITA_TS,
        self::ITA_UD,
        self::ITA_VA,
        self::ITA_VE,
        self::ITA_VB,
        self::ITA_VC,
        self::ITA_VR,
        self::ITA_VV,
        self::ITA_VI,
        self::ITA_VT,
        self::ITA_OT,
    ];

    /**
     * Ensures that all the given values are present in this Enum.
     *
     * @param array|stdClass|null|string $value Value or a list/map of values to be checked
     *
     * @return array|null|string Input value(s), if all are a part of this Enum
     *
     * @throws Exception Throws exception if any given value is not in this Enum
     */
    public static function checkValue($value)
    {
        $value = json_decode(json_encode($value), true); // converts stdClass into array
        ApiHelper::checkValueInEnum($value, self::class, self::_ALL_VALUES);
        return $value;
    }
}
