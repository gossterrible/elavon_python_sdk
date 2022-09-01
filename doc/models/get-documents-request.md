
# Get Documents Request

## Structure

`GetDocumentsRequest`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `profileCode` | `?string` | Optional | The partner's profile code | getProfileCode(): ?string | setProfileCode(?string profileCode): void |
| `documentInputs` | [`?array<string,UserDocumentInput>`](../../doc/models/user-document-input.md) | Optional | The valid key-value pairs are as follows: OPERATING_GUIDE:MerchantOperatingGuideDocumentInput, TERMS_OF_SERVICE:TermsOfServiceDocumentInput, PAY_NAV_MEDICAL_AND_BUSINESS_AGREEMENT:UserDocumentInput, TALECH_ADDENDUM:TalechAddendumDocumentInput, TALECH_ELAVON_TERMS_AND_CONDITION_ADDENDUM:UserDocumentInput, TALECH_TERMS_OF_SERVICE:UserDocumentInput, AMEX_AGREEMENT:AmexDocumentInput, AMEX_TERMS_OF_SERVICE:UserDocumentInput, SAFE_T_ADDENDUM:UserDocumentInput, BLIK_ADDENDUM:BlikAddendumDocumentInput, EPG_TOC:UserDocumentInput, APPLICATION:MerchantAgreementDocumentInput, MERCHANT_AGREEMENT:MerchantAgreementDocumentInput, SIGNED_APPLICATION:MerchantAgreementDocumentInput, UNSIGNED_APPLICATION:MerchantAgreementDocumentInput, DEPOSIT_DIRECT_DEBIT:DirectDebitDocumentInput, DEPOSIT_SIGNED_DIRECT_DEBIT:DirectDebitDocumentInput, BILLING_DIRECT_DEBIT:DirectDebitDocumentInput, BILLING_SIGNED_DIRECT_DEBIT:DirectDebitDocumentInput, CHARGEBACK_DIRECT_DEBIT:DirectDebitDocumentInput, CHARGEBACK_SIGNED_DIRECT_DEBIT:DirectDebitDocumentInput, APPLICATION_ADDENDUM:MerchantAgreementDocumentInput, TERMINAL_HIRE_AGREEMENT:TerminalHireDocumentInput, TERMINAL_HIRE_PRE_CONTRACT:TerminalHireDocumentInput, TERMINAL_HIRE_AGREEMENT_STATUTORY:TerminalHireDocumentInput, CUSTOM_NOTES:CustomNotesDocumentInput, CALIFORNIA_LEASE:LeaseAgreementDocumentInput, LEASE_AGREEMENT:LeaseAgreementDocumentInput, ELAVON_SECURED_PRO_TOC:ElavonPciServiceDocumentInput, ELAVON_SECURED_ENCRYPT_TOC:ElavonPciServiceDocumentInput, EPG_ADDENDUM:ElavonPaymentGatewayAddendumDocumentInput, PROMOTION_ADDENDUM:PolishPromotionAddendumDocumentInput, CANADIAN_CODE_OF_CONDUCT:CanadianCodeOfConductDocumentInput, ELAVON_TOKENIZATION_TOC:ElavonTokenizationTermsAndConditionsDocumentInput, GOVERNMENT_INCENTIVE_ADDENDUM:GovernmentIncentiveAddendumDocumentInput, AMEX_SITE_LETTER:AmexDocumentInput, SELF_GUARANTEE:PersonalGuaranteeDocumentInput, POYNT_ADDENDUM:PoyntAddendumDocumentInput, CONVERGE_ADDENDUM:ConvergeAddendumDocumentInput, SANTANDER_POS_ADDENDUM:SantanderPosAddendumDocumentInput, CONVERGE_ELAVON_TERMS_AND_CONDITION_ADDENDUM:ConvergeTermsAndConditionsAddendumDocumentInput, KKT_ADDENDUM:KktAddendumDocumentInput, OPAYO_TOS:UserDocumentInput, PARTNER_DOCUMENTS:PartnerDocumentInput | getDocumentInputs(): ?array | setDocumentInputs(?array documentInputs): void |
| `html` | `?bool` | Optional | Boolean indicating if return should be encoded as a PDF or HTML. Boolean true for HTML, false for PDF | getHtml(): ?bool | setHtml(?bool html): void |

## Example (as JSON)

```json
{
  "profileCode": null,
  "documentInputs": null,
  "html": null
}
```

