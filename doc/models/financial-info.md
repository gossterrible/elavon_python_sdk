
# Financial Info

## Structure

`FinancialInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `avgSaleAmount` | `string` | Required | Average Transaction Value (ATV) | getAvgSaleAmount(): string | setAvgSaleAmount(string avgSaleAmount): void |
| `monthlyCardSales` | `string` | Required | Predicted monthly credit card sales | getMonthlyCardSales(): string | setMonthlyCardSales(string monthlyCardSales): void |
| `annualCardSales` | `?string` | Optional | [EU] Projected yearly card sales | getAnnualCardSales(): ?string | setAnnualCardSales(?string annualCardSales): void |
| `annualRevenue` | `?string` | Optional | Projected yearly gross revenue | getAnnualRevenue(): ?string | setAnnualRevenue(?string annualRevenue): void |
| `highestTicketAmount` | `?string` | Optional | [NA] Highest estimated ticket amount | getHighestTicketAmount(): ?string | setHighestTicketAmount(?string highestTicketAmount): void |
| `highestTicketFrequency` | `?int` | Optional | [NA] Frequency with which highest ticket is received annually | getHighestTicketFrequency(): ?int | setHighestTicketFrequency(?int highestTicketFrequency): void |
| `fundingCurrency` | `?string` | Optional | Funding currency of business | getFundingCurrency(): ?string | setFundingCurrency(?string fundingCurrency): void |
| `cardPresentAcceptancePercent` | `string` | Required | The percentage split of card present transactions | getCardPresentAcceptancePercent(): string | setCardPresentAcceptancePercent(string cardPresentAcceptancePercent): void |
| `internetAcceptancePercent` | `string` | Required | The percentage split of internet/ecom transactions | getInternetAcceptancePercent(): string | setInternetAcceptancePercent(string internetAcceptancePercent): void |
| `motoAcceptancePercent` | `string` | Required | The percentage split of mail-order/telephone-order transactions | getMotoAcceptancePercent(): string | setMotoAcceptancePercent(string motoAcceptancePercent): void |
| `businessEmailAddress` | `?string` | Optional | [EU] Business email contact, required if internetAcceptancePercent > 0 | getBusinessEmailAddress(): ?string | setBusinessEmailAddress(?string businessEmailAddress): void |
| `businessWebsiteURL` | `?string` | Optional | Business URL, required if internetAcceptancePercent > 0 | getBusinessWebsiteURL(): ?string | setBusinessWebsiteURL(?string businessWebsiteURL): void |
| `customerServicePhone` | [`?PhoneNumber`](../../doc/models/phone-number.md) | Optional | - | getCustomerServicePhone(): ?PhoneNumber | setCustomerServicePhone(?PhoneNumber customerServicePhone): void |
| `notPresentDelayDays` | `?int` | Optional | [NA] Card Not Present delay for something | getNotPresentDelayDays(): ?int | setNotPresentDelayDays(?int notPresentDelayDays): void |
| `depositFrequency` | `?string` | Optional | [EU] | getDepositFrequency(): ?string | setDepositFrequency(?string depositFrequency): void |
| `depositSizePercent` | `?string` | Optional | [EU] | getDepositSizePercent(): ?string | setDepositSizePercent(?string depositSizePercent): void |
| `depositBalanceDays` | `?string` | Optional | [EU] | getDepositBalanceDays(): ?string | setDepositBalanceDays(?string depositBalanceDays): void |
| `depositFulfillmentDays` | `?string` | Optional | [EU] | getDepositFulfillmentDays(): ?string | setDepositFulfillmentDays(?string depositFulfillmentDays): void |
| `fullPaymentPercent` | `?string` | Optional | [EU] | getFullPaymentPercent(): ?string | setFullPaymentPercent(?string fullPaymentPercent): void |
| `fullPaymentFulfillment` | `?string` | Optional | [EU] | getFullPaymentFulfillment(): ?string | setFullPaymentFulfillment(?string fullPaymentFulfillment): void |
| `utilizeCVV2` | `?bool` | Optional | [EU] | getUtilizeCVV2(): ?bool | setUtilizeCVV2(?bool utilizeCVV2): void |
| `recurringTransactions` | `?bool` | Optional | [EU] | getRecurringTransactions(): ?bool | setRecurringTransactions(?bool recurringTransactions): void |
| `contractTermType` | [`?string (ContractTermTypeEnum)`](../../doc/models/contract-term-type-enum.md) | Optional | [EU] ZERO_MONTH, TWELVE_MONTHS, TWENTY_FOUR_MONTHS, or THIRTY_SIX_MONTHS | getContractTermType(): ?string | setContractTermType(?string contractTermType): void |
| `monthsClosed` | [`?(string[]) (MonthsClosedEnum)`](../../doc/models/months-closed-enum.md) | Optional | List containing months business is closed, for seasonal businesses | getMonthsClosed(): ?array | setMonthsClosed(?array monthsClosed): void |
| `monetaryBillingMethod` | [`?string (MonetaryBillingMethodEnum)`](../../doc/models/monetary-billing-method-enum.md) | Optional | [NA] string, CARD_DISCOUNT or DIA | getMonetaryBillingMethod(): ?string | setMonetaryBillingMethod(?string monetaryBillingMethod): void |
| `authorizationIncluded` | `?bool` | Optional | [NA] | getAuthorizationIncluded(): ?bool | setAuthorizationIncluded(?bool authorizationIncluded): void |
| `annualFeeMonthStart` | [`?string (AnnualFeeMonthStartEnum)`](../../doc/models/annual-fee-month-start-enum.md) | Optional | [NA] The month in which annual fee is applied | getAnnualFeeMonthStart(): ?string | setAnnualFeeMonthStart(?string annualFeeMonthStart): void |
| `moneyServices` | `?bool` | Optional | [EU] | getMoneyServices(): ?bool | setMoneyServices(?bool moneyServices): void |
| `paymentServices` | `?bool` | Optional | - | getPaymentServices(): ?bool | setPaymentServices(?bool paymentServices): void |
| `thirdPartyProcessor` | `?bool` | Optional | - | getThirdPartyProcessor(): ?bool | setThirdPartyProcessor(?bool thirdPartyProcessor): void |
| `nonGovernmentNonProfit` | `?bool` | Optional | [EU] | getNonGovernmentNonProfit(): ?bool | setNonGovernmentNonProfit(?bool nonGovernmentNonProfit): void |
| `dailyDiscount` | `?bool` | Optional | [NA] | getDailyDiscount(): ?bool | setDailyDiscount(?bool dailyDiscount): void |
| `nonBankAtm` | `?bool` | Optional | Does business operate its own ATM (not associated with a bank) | getNonBankAtm(): ?bool | setNonBankAtm(?bool nonBankAtm): void |
| `embassy` | `?bool` | Optional | Deprecated | getEmbassy(): ?bool | setEmbassy(?bool embassy): void |
| `highInterAnnualTransNgo` | `?bool` | Optional | Deprecated | getHighInterAnnualTransNgo(): ?bool | setHighInterAnnualTransNgo(?bool highInterAnnualTransNgo): void |

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

