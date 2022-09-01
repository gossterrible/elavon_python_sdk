
# Financial Info

## Structure

`FinancialInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `avg_sale_amount` | `string` | Required | Average Transaction Value (ATV) |
| `monthly_card_sales` | `string` | Required | Predicted monthly credit card sales |
| `annual_card_sales` | `string` | Optional | [EU] Projected yearly card sales |
| `annual_revenue` | `string` | Optional | Projected yearly gross revenue |
| `highest_ticket_amount` | `string` | Optional | [NA] Highest estimated ticket amount |
| `highest_ticket_frequency` | `int` | Optional | [NA] Frequency with which highest ticket is received annually |
| `funding_currency` | `string` | Optional | Funding currency of business |
| `card_present_acceptance_percent` | `string` | Required | The percentage split of card present transactions |
| `internet_acceptance_percent` | `string` | Required | The percentage split of internet/ecom transactions |
| `moto_acceptance_percent` | `string` | Required | The percentage split of mail-order/telephone-order transactions |
| `business_email_address` | `string` | Optional | [EU] Business email contact, required if internetAcceptancePercent > 0 |
| `business_website_url` | `string` | Optional | Business URL, required if internetAcceptancePercent > 0 |
| `customer_service_phone` | [`PhoneNumber`](../../doc/models/phone-number.md) | Optional | - |
| `not_present_delay_days` | `int` | Optional | [NA] Card Not Present delay for something |
| `deposit_frequency` | `string` | Optional | [EU] |
| `deposit_size_percent` | `string` | Optional | [EU] |
| `deposit_balance_days` | `string` | Optional | [EU] |
| `deposit_fulfillment_days` | `string` | Optional | [EU] |
| `full_payment_percent` | `string` | Optional | [EU] |
| `full_payment_fulfillment` | `string` | Optional | [EU] |
| `utilize_cvv_2` | `bool` | Optional | [EU] |
| `recurring_transactions` | `bool` | Optional | [EU] |
| `contract_term_type` | [`ContractTermTypeEnum`](../../doc/models/contract-term-type-enum.md) | Optional | [EU] ZERO_MONTH, TWELVE_MONTHS, TWENTY_FOUR_MONTHS, or THIRTY_SIX_MONTHS |
| `months_closed` | [`List of MonthsClosedEnum`](../../doc/models/months-closed-enum.md) | Optional | List containing months business is closed, for seasonal businesses |
| `monetary_billing_method` | [`MonetaryBillingMethodEnum`](../../doc/models/monetary-billing-method-enum.md) | Optional | [NA] string, CARD_DISCOUNT or DIA |
| `authorization_included` | `bool` | Optional | [NA] |
| `annual_fee_month_start` | [`AnnualFeeMonthStartEnum`](../../doc/models/annual-fee-month-start-enum.md) | Optional | [NA] The month in which annual fee is applied |
| `money_services` | `bool` | Optional | [EU] |
| `payment_services` | `bool` | Optional | - |
| `third_party_processor` | `bool` | Optional | - |
| `non_government_non_profit` | `bool` | Optional | [EU] |
| `daily_discount` | `bool` | Optional | [NA] |
| `non_bank_atm` | `bool` | Optional | Does business operate its own ATM (not associated with a bank) |
| `embassy` | `bool` | Optional | Deprecated |
| `high_inter_annual_trans_ngo` | `bool` | Optional | Deprecated |

## Example (as JSON)

```json
{
  "avgSaleAmount": "125",
  "monthlyCardSales": "1000",
  "cardPresentAcceptancePercent": "100",
  "internetAcceptancePercent": "0",
  "motoAcceptancePercent": "0"
}
```

