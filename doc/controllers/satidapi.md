# SATIDAPI

```php
$sATIDAPIController = $client->getSATIDAPIController();
```

## Class Name

`SATIDAPIController`

## Methods

* [Upload Documents](../../doc/controllers/satidapi.md#upload-documents)
* [Board](../../doc/controllers/satidapi.md#board)
* [Postal Validate](../../doc/controllers/satidapi.md#postal-validate)
* [Bank Validate](../../doc/controllers/satidapi.md#bank-validate)
* [Refresh Signer User Sessions](../../doc/controllers/satidapi.md#refresh-signer-user-sessions)
* [Regenerate Packet Documents](../../doc/controllers/satidapi.md#regenerate-packet-documents)
* [List Packet Presented Documents](../../doc/controllers/satidapi.md#list-packet-presented-documents)
* [Get Signed Document Packet Content](../../doc/controllers/satidapi.md#get-signed-document-packet-content)
* [Generate Packet Documents](../../doc/controllers/satidapi.md#generate-packet-documents)
* [Board Xsd Schema](../../doc/controllers/satidapi.md#board-xsd-schema)
* [Credit Check Xsd Schema](../../doc/controllers/satidapi.md#credit-check-xsd-schema)
* [Board Status Xsd Schema](../../doc/controllers/satidapi.md#board-status-xsd-schema)
* [Upload Document Xsd Schema](../../doc/controllers/satidapi.md#upload-document-xsd-schema)
* [Post Code Xsd Schema](../../doc/controllers/satidapi.md#post-code-xsd-schema)
* [Bank Xsd Schema](../../doc/controllers/satidapi.md#bank-xsd-schema)
* [Get Quiz Xsd Schema](../../doc/controllers/satidapi.md#get-quiz-xsd-schema)
* [Answer Quiz Xsd Schema](../../doc/controllers/satidapi.md#answer-quiz-xsd-schema)
* [Get Quiz](../../doc/controllers/satidapi.md#get-quiz)
* [Answer Quiz](../../doc/controllers/satidapi.md#answer-quiz)
* [List Presented Documents](../../doc/controllers/satidapi.md#list-presented-documents)
* [Get Presented Documents](../../doc/controllers/satidapi.md#get-presented-documents)
* [Board Status](../../doc/controllers/satidapi.md#board-status)
* [Get Terminal Ids](../../doc/controllers/satidapi.md#get-terminal-ids)
* [Create Group Document Packet](../../doc/controllers/satidapi.md#create-group-document-packet)
* [Append Group Document Packet](../../doc/controllers/satidapi.md#append-group-document-packet)
* [Create Document Packet](../../doc/controllers/satidapi.md#create-document-packet)
* [Credit Check](../../doc/controllers/satidapi.md#credit-check)
* [Update Document Packet Data](../../doc/controllers/satidapi.md#update-document-packet-data)
* [Check Document Signing Status](../../doc/controllers/satidapi.md#check-document-signing-status)
* [Delete Document Packet](../../doc/controllers/satidapi.md#delete-document-packet)
* [Delete Group Document Packet](../../doc/controllers/satidapi.md#delete-group-document-packet)
* [Update Document Packet](../../doc/controllers/satidapi.md#update-document-packet)
* [Execute Group Document Packet](../../doc/controllers/satidapi.md#execute-group-document-packet)
* [Get Unsigned Document Content](../../doc/controllers/satidapi.md#get-unsigned-document-content)
* [Get Unsigned Documents Packet Content](../../doc/controllers/satidapi.md#get-unsigned-documents-packet-content)


# Upload Documents

Upload Documents

```php
function uploadDocuments(int $versionNumber, UploadDocumentsRequestParams $body): UploadDocumentResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `versionNumber` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |
| `body` | [`UploadDocumentsRequestParams`](../../doc/models/upload-documents-request-params.md) | Body, Required | - |

## Response Type

[`UploadDocumentResponse`](../../doc/models/upload-document-response.md)

## Example Usage

```php
$versionNumber = 66;
$body_boardingId = '2101491576';
$body_clientId = 'IDNA';
$body_uniqueId = 'AcmeCorp1572566399123';
$body_country = 'country0';
$body_salesRepNumber = '12345';
$body_imageDocumentData_docReferenceNumber = 'docReferenceNumber4';
$body_imageDocumentData_imageDocuments = [];

$body_imageDocumentData_imageDocuments_0_imageId = 208;
$body_imageDocumentData_imageDocuments_0_imageTypeCode = 'APPLI';
$body_imageDocumentData_imageDocuments_0_dbaName = 'Grimm\'s Bookstore';
$body_imageDocumentData_imageDocuments_0_mimeTypeCode = Models\MimeTypeCodeEnum::JPG;
$body_imageDocumentData_imageDocuments_0_imageContent = ['imageContent4', 'imageContent5', 'imageContent6'];
$body_imageDocumentData_imageDocuments[0] = new Models\ImageDocument(
    $body_imageDocumentData_imageDocuments_0_imageId,
    $body_imageDocumentData_imageDocuments_0_imageTypeCode,
    $body_imageDocumentData_imageDocuments_0_dbaName,
    $body_imageDocumentData_imageDocuments_0_mimeTypeCode,
    $body_imageDocumentData_imageDocuments_0_imageContent
);

$body_imageDocumentData_imageDocuments_1_imageId = 209;
$body_imageDocumentData_imageDocuments_1_imageTypeCode = 'APPLI';
$body_imageDocumentData_imageDocuments_1_dbaName = 'Grimm\'s Bookstore';
$body_imageDocumentData_imageDocuments_1_mimeTypeCode = Models\MimeTypeCodeEnum::PDF;
$body_imageDocumentData_imageDocuments_1_imageContent = ['imageContent5'];
$body_imageDocumentData_imageDocuments[1] = new Models\ImageDocument(
    $body_imageDocumentData_imageDocuments_1_imageId,
    $body_imageDocumentData_imageDocuments_1_imageTypeCode,
    $body_imageDocumentData_imageDocuments_1_dbaName,
    $body_imageDocumentData_imageDocuments_1_mimeTypeCode,
    $body_imageDocumentData_imageDocuments_1_imageContent
);

$body_imageDocumentData_imageDocuments_2_imageId = 210;
$body_imageDocumentData_imageDocuments_2_imageTypeCode = 'APPLI';
$body_imageDocumentData_imageDocuments_2_dbaName = 'Grimm\'s Bookstore';
$body_imageDocumentData_imageDocuments_2_mimeTypeCode = Models\MimeTypeCodeEnum::SVG;
$body_imageDocumentData_imageDocuments_2_imageContent = ['imageContent6', 'imageContent7'];
$body_imageDocumentData_imageDocuments[2] = new Models\ImageDocument(
    $body_imageDocumentData_imageDocuments_2_imageId,
    $body_imageDocumentData_imageDocuments_2_imageTypeCode,
    $body_imageDocumentData_imageDocuments_2_dbaName,
    $body_imageDocumentData_imageDocuments_2_mimeTypeCode,
    $body_imageDocumentData_imageDocuments_2_imageContent
);

$body_imageDocumentData = new Models\ImageDocumentData(
    $body_imageDocumentData_docReferenceNumber,
    $body_imageDocumentData_imageDocuments
);
$body = new Models\UploadDocumentsRequestParams(
    $body_boardingId,
    $body_clientId,
    $body_uniqueId,
    $body_country,
    $body_salesRepNumber,
    $body_imageDocumentData
);

$result = $sATIDAPIController->uploadDocuments($versionNumber, $body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Board

Boarding

```php
function board(int $versionNumber, BoardingRequestParams $body): BoardingResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `versionNumber` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-4]` |
| `body` | [`BoardingRequestParams`](../../doc/models/boarding-request-params.md) | Body, Required | - |

## Response Type

[`BoardingResponse`](../../doc/models/boarding-response.md)

## Example Usage

```php
$versionNumber = 66;
$body_scarecrowApplication_clientId = 'IDNA';
$body_scarecrowApplication_uniqueId = 'AcmeCorp1572566399123';
$body_scarecrowApplication_country = 'USA';
$body_scarecrowApplication_principal_name_firstName = 'John';
$body_scarecrowApplication_principal_name_lastName = 'Doe';
$body_scarecrowApplication_principal_name = new Models\Name(
    $body_scarecrowApplication_principal_name_firstName,
    $body_scarecrowApplication_principal_name_lastName
);
$body_scarecrowApplication_principal_positions = ['key0' => false, 'key1' => true, 'key2' => false];
$body_scarecrowApplication_principal = new Models\Person(
    $body_scarecrowApplication_principal_name,
    $body_scarecrowApplication_principal_positions
);
$body_scarecrowApplication_businessInfo_dbaName = 'Grimm\'s Bookstore';
$body_scarecrowApplication_businessInfo_dbaNameExtended = 'Grimm\'s Fairytales and Other Stories Bookstore';
$body_scarecrowApplication_businessInfo_businessAddress_streetName = 'Baker Street';
$body_scarecrowApplication_businessInfo_businessAddress_city = 'Atlanta';
$body_scarecrowApplication_businessInfo_businessAddress_country = 'USA';
$body_scarecrowApplication_businessInfo_businessAddress = new Models\Address(
    $body_scarecrowApplication_businessInfo_businessAddress_streetName,
    $body_scarecrowApplication_businessInfo_businessAddress_city,
    $body_scarecrowApplication_businessInfo_businessAddress_country
);
$body_scarecrowApplication_businessInfo_legalName = 'Barkers Dog Bakery';
$body_scarecrowApplication_businessInfo_legalNameExtended = 'Baking Better Biscuits for Your Favorite Barkers Dog Bakery LLC';
$body_scarecrowApplication_businessInfo_additionalAddresses = [];

$body_scarecrowApplication_businessInfo_additionalAddresses__streetName = null;
$body_scarecrowApplication_businessInfo_additionalAddresses__city = null;
$body_scarecrowApplication_businessInfo_additionalAddresses__country = null;
$body_scarecrowApplication_businessInfo_additionalAddresses[''] = new Models\Address(
    $body_scarecrowApplication_businessInfo_additionalAddresses__streetName,
    $body_scarecrowApplication_businessInfo_additionalAddresses__city,
    $body_scarecrowApplication_businessInfo_additionalAddresses__country
);

$body_scarecrowApplication_businessInfo_additionalAddresses__streetName = null;
$body_scarecrowApplication_businessInfo_additionalAddresses__city = null;
$body_scarecrowApplication_businessInfo_additionalAddresses__country = null;
$body_scarecrowApplication_businessInfo_additionalAddresses[''] = new Models\Address(
    $body_scarecrowApplication_businessInfo_additionalAddresses__streetName,
    $body_scarecrowApplication_businessInfo_additionalAddresses__city,
    $body_scarecrowApplication_businessInfo_additionalAddresses__country
);

$body_scarecrowApplication_businessInfo_additionalAddresses__streetName = null;
$body_scarecrowApplication_businessInfo_additionalAddresses__city = null;
$body_scarecrowApplication_businessInfo_additionalAddresses__country = null;
$body_scarecrowApplication_businessInfo_additionalAddresses[''] = new Models\Address(
    $body_scarecrowApplication_businessInfo_additionalAddresses__streetName,
    $body_scarecrowApplication_businessInfo_additionalAddresses__city,
    $body_scarecrowApplication_businessInfo_additionalAddresses__country
);

$body_scarecrowApplication_businessInfo_ownershipType = Models\OwnershipTypeEnum::PARTNERSHIP_LIMITED_BY_SHARES;
$body_scarecrowApplication_businessInfo_productDescription = 'Bakeries';
$body_scarecrowApplication_businessInfo_mccCode = '7399E';
$body_scarecrowApplication_businessInfo_establishmentYear = '2005';
$body_scarecrowApplication_businessInfo_currentOwnershipYears = '3';
$body_scarecrowApplication_businessInfo_currentOwnershipMonths = '6';
$body_scarecrowApplication_businessInfo_communicationLanguage = 'en';
$body_scarecrowApplication_businessInfo_posLanguage = 'en';
$body_scarecrowApplication_businessInfo = new Models\BusinessInfo(
    $body_scarecrowApplication_businessInfo_dbaName,
    $body_scarecrowApplication_businessInfo_dbaNameExtended,
    $body_scarecrowApplication_businessInfo_businessAddress,
    $body_scarecrowApplication_businessInfo_legalName,
    $body_scarecrowApplication_businessInfo_legalNameExtended,
    $body_scarecrowApplication_businessInfo_additionalAddresses,
    $body_scarecrowApplication_businessInfo_ownershipType,
    $body_scarecrowApplication_businessInfo_productDescription,
    $body_scarecrowApplication_businessInfo_mccCode,
    $body_scarecrowApplication_businessInfo_establishmentYear,
    $body_scarecrowApplication_businessInfo_currentOwnershipYears,
    $body_scarecrowApplication_businessInfo_currentOwnershipMonths,
    $body_scarecrowApplication_businessInfo_communicationLanguage,
    $body_scarecrowApplication_businessInfo_posLanguage
);
$body_scarecrowApplication_financialInfo_avgSaleAmount = '125';
$body_scarecrowApplication_financialInfo_monthlyCardSales = '1000';
$body_scarecrowApplication_financialInfo_cardPresentAcceptancePercent = '100';
$body_scarecrowApplication_financialInfo_internetAcceptancePercent = '0';
$body_scarecrowApplication_financialInfo_motoAcceptancePercent = '0';
$body_scarecrowApplication_financialInfo = new Models\FinancialInfo(
    $body_scarecrowApplication_financialInfo_avgSaleAmount,
    $body_scarecrowApplication_financialInfo_monthlyCardSales,
    $body_scarecrowApplication_financialInfo_cardPresentAcceptancePercent,
    $body_scarecrowApplication_financialInfo_internetAcceptancePercent,
    $body_scarecrowApplication_financialInfo_motoAcceptancePercent
);
$body_scarecrowApplication_salesRepCode = '12345';
$body_scarecrowApplication_contact_name_firstName = 'John';
$body_scarecrowApplication_contact_name_lastName = 'Doe';
$body_scarecrowApplication_contact_name = new Models\Name(
    $body_scarecrowApplication_contact_name_firstName,
    $body_scarecrowApplication_contact_name_lastName
);
$body_scarecrowApplication_contact_positions = ['key0' => false, 'key1' => true];
$body_scarecrowApplication_contact = new Models\Person(
    $body_scarecrowApplication_contact_name,
    $body_scarecrowApplication_contact_positions
);
$body_scarecrowApplication_bankAccounts = [];

$body_scarecrowApplication_bankAccounts__fundingMethod = envrr;
$body_scarecrowApplication_bankAccounts__accountNumber = null;
$body_scarecrowApplication_bankAccounts__sortCode = null;
$body_scarecrowApplication_bankAccounts[''] = new Models\BankingInfo(
    $body_scarecrowApplication_bankAccounts__fundingMethod,
    $body_scarecrowApplication_bankAccounts__accountNumber,
    $body_scarecrowApplication_bankAccounts__sortCode
);

$body_scarecrowApplication_cardPricing_pricingMethod = Models\PricingMethodEnum::ASSOCIATION;
$body_scarecrowApplication_cardPricing_pricingCategory = Models\PricingCategoryEnum::MOTO;
$body_scarecrowApplication_cardPricing_cardCharges = [];

$body_scarecrowApplication_cardPricing_cardCharges_0_cardType = Models\CardTypeEnum::VISA_DEBIT;
$body_scarecrowApplication_cardPricing_cardCharges[0] = new Models\CardCharge(
    $body_scarecrowApplication_cardPricing_cardCharges_0_cardType
);

$body_scarecrowApplication_cardPricing = new Models\CardPricing(
    $body_scarecrowApplication_cardPricing_pricingMethod,
    $body_scarecrowApplication_cardPricing_pricingCategory,
    $body_scarecrowApplication_cardPricing_cardCharges
);
$body_scarecrowApplication_parentEntity = 'parentEntity8';
$body_scarecrowApplication = new Models\ScarecrowApplication(
    $body_scarecrowApplication_clientId,
    $body_scarecrowApplication_uniqueId,
    $body_scarecrowApplication_country,
    $body_scarecrowApplication_principal,
    $body_scarecrowApplication_businessInfo,
    $body_scarecrowApplication_financialInfo,
    $body_scarecrowApplication_salesRepCode,
    $body_scarecrowApplication_contact,
    $body_scarecrowApplication_bankAccounts,
    $body_scarecrowApplication_cardPricing,
    $body_scarecrowApplication_parentEntity
);
$body = new Models\BoardingRequestParams(
    $body_scarecrowApplication
);

$result = $sATIDAPIController->board($versionNumber, $body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Postal Validate

Validate Postal Code

```php
function postalValidate(int $versionNumber, ValidateZipCodeRequest $body): ValidateZipCodeRequest
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `versionNumber` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |
| `body` | [`ValidateZipCodeRequest`](../../doc/models/validate-zip-code-request.md) | Body, Required | - |

## Response Type

[`ValidateZipCodeRequest`](../../doc/models/validate-zip-code-request.md)

## Example Usage

```php
$versionNumber = 66;
$body_zipCode = '20330';
$body_country = 'USA';
$body = new Models\ValidateZipCodeRequest(
    $body_zipCode,
    $body_country
);

$result = $sATIDAPIController->postalValidate($versionNumber, $body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Bank Validate

Validate Bank Account

```php
function bankValidate(int $versionNumber, BankingInfo $body): VerifyBankAccountResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `versionNumber` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |
| `body` | [`BankingInfo`](../../doc/models/banking-info.md) | Body, Required | - |

## Response Type

[`VerifyBankAccountResponse`](../../doc/models/verify-bank-account-response.md)

## Example Usage

```php
$versionNumber = 66;
$body_fundingMethod = Models\FundingMethodEnum::NETCREDIT;
$body_accountNumber = '20581687';
$body_sortCode = '121000248';
$body = new Models\BankingInfo(
    $body_fundingMethod,
    $body_accountNumber,
    $body_sortCode
);

$result = $sATIDAPIController->bankValidate($versionNumber, $body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Refresh Signer User Sessions

Refresh the session for signers of a document packet

```php
function refreshSignerUserSessions(RefreshSignerUsersSessionsRequest $body): RefershSignerUserSessionsResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RefreshSignerUsersSessionsRequest`](../../doc/models/refresh-signer-users-sessions-request.md) | Body, Required | - |

## Response Type

[`RefershSignerUserSessionsResponse`](../../doc/models/refersh-signer-user-sessions-response.md)

## Example Usage

```php
$body_documentPacketId = '42f441d0-0c23-468d-8319-f1e2af17dc15';
$body_signerIds = ['signerIds5', 'signerIds6', 'signerIds7'];
$body = new Models\RefreshSignerUsersSessionsRequest(
    $body_documentPacketId,
    $body_signerIds
);

$result = $sATIDAPIController->refreshSignerUserSessions($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Regenerate Packet Documents

Regenerate signed Packet Content in event of failure

```php
function regeneratePacketDocuments(RegenerateDocumentPacketRequest $body): Response
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RegenerateDocumentPacketRequest`](../../doc/models/regenerate-document-packet-request.md) | Body, Required | - |

## Response Type

[`Response`](../../doc/models/response.md)

## Example Usage

```php
$body_documentPacketId = 'documentPacketId2';
$body = new Models\RegenerateDocumentPacketRequest(
    $body_documentPacketId
);

$result = $sATIDAPIController->regeneratePacketDocuments($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# List Packet Presented Documents

List Packet Documents to present to the user

```php
function listPacketPresentedDocuments(ListPacketDocumentsRequest $body): ListDocumentsResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ListPacketDocumentsRequest`](../../doc/models/list-packet-documents-request.md) | Body, Required | - |

## Response Type

[`ListDocumentsResponse`](../../doc/models/list-documents-response.md)

## Example Usage

```php
$body = new Models\ListPacketDocumentsRequest;

$result = $sATIDAPIController->listPacketPresentedDocuments($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Get Signed Document Packet Content

Get signed document packet content

```php
function getSignedDocumentPacketContent(GetSignedDocumentPacketRequest $body): GetDocumentsResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetSignedDocumentPacketRequest`](../../doc/models/get-signed-document-packet-request.md) | Body, Required | - |

## Response Type

[`GetDocumentsResponse`](../../doc/models/get-documents-response.md)

## Example Usage

```php
$body = new Models\GetSignedDocumentPacketRequest;

$result = $sATIDAPIController->getSignedDocumentPacketContent($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Generate Packet Documents

Trigger generation of document in packet for submission

```php
function generatePacketDocuments(GeneratePacketDocumentsRequest $body): GeneratePacketDocumentsResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GeneratePacketDocumentsRequest`](../../doc/models/generate-packet-documents-request.md) | Body, Required | - |

## Response Type

[`GeneratePacketDocumentsResponse`](../../doc/models/generate-packet-documents-response.md)

## Example Usage

```php
$body = new Models\GeneratePacketDocumentsRequest;

$result = $sATIDAPIController->generatePacketDocuments($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Board Xsd Schema

Get Boarding Schema

```php
function boardXsdSchema(int $versionNumber, string $iso3Country): void
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `versionNumber` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-4]` |
| `iso3Country` | `string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```php
$versionNumber = 66;
$iso3Country = 'iso3Country6';

$sATIDAPIController->boardXsdSchema($versionNumber, $iso3Country);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | successful operation | `ApiException` |


# Credit Check Xsd Schema

Get Credit Check Schema

```php
function creditCheckXsdSchema(int $versionNumber, string $iso3Country): void
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `versionNumber` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-4]` |
| `iso3Country` | `string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```php
$versionNumber = 66;
$iso3Country = 'iso3Country6';

$sATIDAPIController->creditCheckXsdSchema($versionNumber, $iso3Country);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | successful operation | `ApiException` |


# Board Status Xsd Schema

Get Boarding Status Schema

```php
function boardStatusXsdSchema(int $versionNumber): void
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `versionNumber` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |

## Response Type

`void`

## Example Usage

```php
$versionNumber = 66;

$sATIDAPIController->boardStatusXsdSchema($versionNumber);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | successful operation | `ApiException` |


# Upload Document Xsd Schema

Get Upload Documents Schema

```php
function uploadDocumentXsdSchema(int $versionNumber): void
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `versionNumber` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |

## Response Type

`void`

## Example Usage

```php
$versionNumber = 66;

$sATIDAPIController->uploadDocumentXsdSchema($versionNumber);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | successful operation | `ApiException` |


# Post Code Xsd Schema

Get Postal Code Validation Schema

```php
function postCodeXsdSchema(int $versionNumber): void
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `versionNumber` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |

## Response Type

`void`

## Example Usage

```php
$versionNumber = 66;

$sATIDAPIController->postCodeXsdSchema($versionNumber);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | successful operation | `ApiException` |


# Bank Xsd Schema

Get Bank Account Validation Schema

```php
function bankXsdSchema(int $versionNumber): void
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `versionNumber` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |

## Response Type

`void`

## Example Usage

```php
$versionNumber = 66;

$sATIDAPIController->bankXsdSchema($versionNumber);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | successful operation | `ApiException` |


# Get Quiz Xsd Schema

Get Quiz Request Schema

```php
function getQuizXsdSchema(int $versionNumber): void
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `versionNumber` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |

## Response Type

`void`

## Example Usage

```php
$versionNumber = 66;

$sATIDAPIController->getQuizXsdSchema($versionNumber);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | successful operation | `ApiException` |


# Answer Quiz Xsd Schema

Get Quiz Answer Schema

```php
function answerQuizXsdSchema(int $versionNumber): void
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `versionNumber` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |

## Response Type

`void`

## Example Usage

```php
$versionNumber = 66;

$sATIDAPIController->answerQuizXsdSchema($versionNumber);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | successful operation | `ApiException` |


# Get Quiz

Request KYC Quiz

```php
function getQuiz(int $versionNumber, GetQuizRequest $body): GetQuizResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `versionNumber` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |
| `body` | [`GetQuizRequest`](../../doc/models/get-quiz-request.md) | Body, Required | - |

## Response Type

[`GetQuizResponse`](../../doc/models/get-quiz-response.md)

## Example Usage

```php
$versionNumber = 66;
$body_principal_name_firstName = 'John';
$body_principal_name_lastName = 'Doe';
$body_principal_name = new Models\Name(
    $body_principal_name_firstName,
    $body_principal_name_lastName
);
$body_principal_positions = ['key0' => false];
$body_principal = new Models\Person(
    $body_principal_name,
    $body_principal_positions
);
$body_businessAddress_streetName = 'Baker Street';
$body_businessAddress_city = 'Atlanta';
$body_businessAddress_country = 'USA';
$body_businessAddress = new Models\Address(
    $body_businessAddress_streetName,
    $body_businessAddress_city,
    $body_businessAddress_country
);
$body_language = 'en';
$body = new Models\GetQuizRequest(
    $body_principal,
    $body_businessAddress,
    $body_language
);

$result = $sATIDAPIController->getQuiz($versionNumber, $body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Answer Quiz

Answer KYC Quiz

```php
function answerQuiz(int $versionNumber, AnswerQuizRequest $body): AnswerQuizResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `versionNumber` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |
| `body` | [`AnswerQuizRequest`](../../doc/models/answer-quiz-request.md) | Body, Required | - |

## Response Type

[`AnswerQuizResponse`](../../doc/models/answer-quiz-response.md)

## Example Usage

```php
$versionNumber = 66;
$body_quizId = 162;
$body_transactionKey = 'transactionKey8';
$body_quizAnswers = [];

$body_quizAnswers_0_questionNumber = 30;
$body_quizAnswers_0_answerNumber = 20;
$body_quizAnswers[0] = new Models\QuizAnswer(
    $body_quizAnswers_0_questionNumber,
    $body_quizAnswers_0_answerNumber
);

$body_quizAnswers_1_questionNumber = 31;
$body_quizAnswers_1_answerNumber = 21;
$body_quizAnswers[1] = new Models\QuizAnswer(
    $body_quizAnswers_1_questionNumber,
    $body_quizAnswers_1_answerNumber
);

$body = new Models\AnswerQuizRequest(
    $body_quizId,
    $body_transactionKey,
    $body_quizAnswers
);

$result = $sATIDAPIController->answerQuiz($versionNumber, $body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# List Presented Documents

List Documents to present to the user

```php
function listPresentedDocuments(ListDocumentsRequest $body): ListDocumentsResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ListDocumentsRequest`](../../doc/models/list-documents-request.md) | Body, Required | - |

## Response Type

[`ListDocumentsResponse`](../../doc/models/list-documents-response.md)

## Example Usage

```php
$body = new Models\ListDocumentsRequest;

$result = $sATIDAPIController->listPresentedDocuments($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Get Presented Documents

Get all documents to present to the user

```php
function getPresentedDocuments(GetDocumentsRequest $body): GetDocumentsResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetDocumentsRequest`](../../doc/models/get-documents-request.md) | Body, Required | - |

## Response Type

[`GetDocumentsResponse`](../../doc/models/get-documents-response.md)

## Example Usage

```php
$body = new Models\GetDocumentsRequest;

$result = $sATIDAPIController->getPresentedDocuments($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Board Status

Boarding Status

```php
function boardStatus(int $versionNumber, BoardingStatusRequestParams $body): BoardingStatusResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `versionNumber` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |
| `body` | [`BoardingStatusRequestParams`](../../doc/models/boarding-status-request-params.md) | Body, Required | - |

## Response Type

[`BoardingStatusResponse`](../../doc/models/boarding-status-response.md)

## Example Usage

```php
$versionNumber = 66;
$body_clientId = 'IDNA';
$body_uniqueId = 'AcmeCorp1572566399123';
$body_country = 'USA';
$body_salesRepCode = 'salesRepCode2';
$body = new Models\BoardingStatusRequestParams(
    $body_clientId,
    $body_uniqueId,
    $body_country,
    $body_salesRepCode
);

$result = $sATIDAPIController->boardStatus($versionNumber, $body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Get Terminal Ids

Get terminal ids and related information for MID

```php
function getTerminalIds(GetTerminalIdsRequest $body): GetTerminalIdsResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetTerminalIdsRequest`](../../doc/models/get-terminal-ids-request.md) | Body, Required | - |

## Response Type

[`GetTerminalIdsResponse`](../../doc/models/get-terminal-ids-response.md)

## Example Usage

```php
$body = new Models\GetTerminalIdsRequest;

$result = $sATIDAPIController->getTerminalIds($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Create Group Document Packet

Create Group Document Packet

```php
function createGroupDocumentPacket(CreateGroupDocumentPacketRequest $body): CreateGroupDocumentPacketResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateGroupDocumentPacketRequest`](../../doc/models/create-group-document-packet-request.md) | Body, Required | - |

## Response Type

[`CreateGroupDocumentPacketResponse`](../../doc/models/create-group-document-packet-response.md)

## Example Usage

```php
$body = new Models\CreateGroupDocumentPacketRequest;

$result = $sATIDAPIController->createGroupDocumentPacket($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Append Group Document Packet

Append to Group Document Packet

```php
function appendGroupDocumentPacket(AppendGroupDocumentPacketRequest $body): AppendGroupDocumentPacketResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AppendGroupDocumentPacketRequest`](../../doc/models/append-group-document-packet-request.md) | Body, Required | - |

## Response Type

[`AppendGroupDocumentPacketResponse`](../../doc/models/append-group-document-packet-response.md)

## Example Usage

```php
$body_groupDocumentPacketId = 'groupDocumentPacketId4';
$body_profileCode = 'profileCode8';
$body_signers = [];

$body_signers_0_signerId = 'signerId4';
$body_signers_0_signer_firstName = 'John';
$body_signers_0_signer_lastName = 'Doe';
$body_signers_0_signer = new Models\Name(
    $body_signers_0_signer_firstName,
    $body_signers_0_signer_lastName
);
$body_signers_0_principal = false;
$body_signers[0] = new Models\Signer(
    $body_signers_0_signerId,
    $body_signers_0_signer,
    $body_signers_0_principal
);

$body_signers_1_signerId = 'signerId5';
$body_signers_1_signer_firstName = 'John';
$body_signers_1_signer_lastName = 'Doe';
$body_signers_1_signer = new Models\Name(
    $body_signers_1_signer_firstName,
    $body_signers_1_signer_lastName
);
$body_signers_1_principal = true;
$body_signers[1] = new Models\Signer(
    $body_signers_1_signerId,
    $body_signers_1_signer,
    $body_signers_1_principal
);

$body_signers_2_signerId = 'signerId6';
$body_signers_2_signer_firstName = 'John';
$body_signers_2_signer_lastName = 'Doe';
$body_signers_2_signer = new Models\Name(
    $body_signers_2_signer_firstName,
    $body_signers_2_signer_lastName
);
$body_signers_2_principal = false;
$body_signers[2] = new Models\Signer(
    $body_signers_2_signerId,
    $body_signers_2_signer,
    $body_signers_2_principal
);

$body_documentPacketData_scarecrowApplication_clientId = 'IDNA';
$body_documentPacketData_scarecrowApplication_uniqueId = 'AcmeCorp1572566399123';
$body_documentPacketData_scarecrowApplication_country = 'USA';
$body_documentPacketData_scarecrowApplication_principal_name_firstName = 'John';
$body_documentPacketData_scarecrowApplication_principal_name_lastName = 'Doe';
$body_documentPacketData_scarecrowApplication_principal_name = new Models\Name(
    $body_documentPacketData_scarecrowApplication_principal_name_firstName,
    $body_documentPacketData_scarecrowApplication_principal_name_lastName
);
$body_documentPacketData_scarecrowApplication_principal_positions = ['key0' => false, 'key1' => true, 'key2' => false];
$body_documentPacketData_scarecrowApplication_principal = new Models\Person(
    $body_documentPacketData_scarecrowApplication_principal_name,
    $body_documentPacketData_scarecrowApplication_principal_positions
);
$body_documentPacketData_scarecrowApplication_businessInfo_dbaName = 'Grimm\'s Bookstore';
$body_documentPacketData_scarecrowApplication_businessInfo_dbaNameExtended = 'Grimm\'s Fairytales and Other Stories Bookstore';
$body_documentPacketData_scarecrowApplication_businessInfo_businessAddress_streetName = 'Baker Street';
$body_documentPacketData_scarecrowApplication_businessInfo_businessAddress_city = 'Atlanta';
$body_documentPacketData_scarecrowApplication_businessInfo_businessAddress_country = 'USA';
$body_documentPacketData_scarecrowApplication_businessInfo_businessAddress = new Models\Address(
    $body_documentPacketData_scarecrowApplication_businessInfo_businessAddress_streetName,
    $body_documentPacketData_scarecrowApplication_businessInfo_businessAddress_city,
    $body_documentPacketData_scarecrowApplication_businessInfo_businessAddress_country
);
$body_documentPacketData_scarecrowApplication_businessInfo_legalName = 'Barkers Dog Bakery';
$body_documentPacketData_scarecrowApplication_businessInfo_legalNameExtended = 'Baking Better Biscuits for Your Favorite Barkers Dog Bakery LLC';
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses = [];

$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__streetName = null;
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__city = null;
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__country = null;
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses[''] = new Models\Address(
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__streetName,
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__city,
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__country
);

$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__streetName = null;
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__city = null;
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__country = null;
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses[''] = new Models\Address(
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__streetName,
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__city,
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__country
);

$body_documentPacketData_scarecrowApplication_businessInfo_ownershipType = Models\OwnershipTypeEnum::LIMITED_PARTNERSHIP;
$body_documentPacketData_scarecrowApplication_businessInfo_productDescription = 'Bakeries';
$body_documentPacketData_scarecrowApplication_businessInfo_mccCode = '7399E';
$body_documentPacketData_scarecrowApplication_businessInfo_establishmentYear = '2005';
$body_documentPacketData_scarecrowApplication_businessInfo_currentOwnershipYears = '3';
$body_documentPacketData_scarecrowApplication_businessInfo_currentOwnershipMonths = '6';
$body_documentPacketData_scarecrowApplication_businessInfo_communicationLanguage = 'en';
$body_documentPacketData_scarecrowApplication_businessInfo_posLanguage = 'en';
$body_documentPacketData_scarecrowApplication_businessInfo = new Models\BusinessInfo(
    $body_documentPacketData_scarecrowApplication_businessInfo_dbaName,
    $body_documentPacketData_scarecrowApplication_businessInfo_dbaNameExtended,
    $body_documentPacketData_scarecrowApplication_businessInfo_businessAddress,
    $body_documentPacketData_scarecrowApplication_businessInfo_legalName,
    $body_documentPacketData_scarecrowApplication_businessInfo_legalNameExtended,
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses,
    $body_documentPacketData_scarecrowApplication_businessInfo_ownershipType,
    $body_documentPacketData_scarecrowApplication_businessInfo_productDescription,
    $body_documentPacketData_scarecrowApplication_businessInfo_mccCode,
    $body_documentPacketData_scarecrowApplication_businessInfo_establishmentYear,
    $body_documentPacketData_scarecrowApplication_businessInfo_currentOwnershipYears,
    $body_documentPacketData_scarecrowApplication_businessInfo_currentOwnershipMonths,
    $body_documentPacketData_scarecrowApplication_businessInfo_communicationLanguage,
    $body_documentPacketData_scarecrowApplication_businessInfo_posLanguage
);
$body_documentPacketData_scarecrowApplication_financialInfo_avgSaleAmount = '125';
$body_documentPacketData_scarecrowApplication_financialInfo_monthlyCardSales = '1000';
$body_documentPacketData_scarecrowApplication_financialInfo_cardPresentAcceptancePercent = '100';
$body_documentPacketData_scarecrowApplication_financialInfo_internetAcceptancePercent = '0';
$body_documentPacketData_scarecrowApplication_financialInfo_motoAcceptancePercent = '0';
$body_documentPacketData_scarecrowApplication_financialInfo = new Models\FinancialInfo(
    $body_documentPacketData_scarecrowApplication_financialInfo_avgSaleAmount,
    $body_documentPacketData_scarecrowApplication_financialInfo_monthlyCardSales,
    $body_documentPacketData_scarecrowApplication_financialInfo_cardPresentAcceptancePercent,
    $body_documentPacketData_scarecrowApplication_financialInfo_internetAcceptancePercent,
    $body_documentPacketData_scarecrowApplication_financialInfo_motoAcceptancePercent
);
$body_documentPacketData_scarecrowApplication_salesRepCode = '12345';
$body_documentPacketData_scarecrowApplication_contact_name_firstName = 'John';
$body_documentPacketData_scarecrowApplication_contact_name_lastName = 'Doe';
$body_documentPacketData_scarecrowApplication_contact_name = new Models\Name(
    $body_documentPacketData_scarecrowApplication_contact_name_firstName,
    $body_documentPacketData_scarecrowApplication_contact_name_lastName
);
$body_documentPacketData_scarecrowApplication_contact_positions = ['key0' => false, 'key1' => true];
$body_documentPacketData_scarecrowApplication_contact = new Models\Person(
    $body_documentPacketData_scarecrowApplication_contact_name,
    $body_documentPacketData_scarecrowApplication_contact_positions
);
$body_documentPacketData_scarecrowApplication_bankAccounts = [];

$body_documentPacketData_scarecrowApplication_bankAccounts__fundingMethod = envrr;
$body_documentPacketData_scarecrowApplication_bankAccounts__accountNumber = null;
$body_documentPacketData_scarecrowApplication_bankAccounts__sortCode = null;
$body_documentPacketData_scarecrowApplication_bankAccounts[''] = new Models\BankingInfo(
    $body_documentPacketData_scarecrowApplication_bankAccounts__fundingMethod,
    $body_documentPacketData_scarecrowApplication_bankAccounts__accountNumber,
    $body_documentPacketData_scarecrowApplication_bankAccounts__sortCode
);

$body_documentPacketData_scarecrowApplication_cardPricing_pricingMethod = Models\PricingMethodEnum::TIERED_PRICING;
$body_documentPacketData_scarecrowApplication_cardPricing_pricingCategory = Models\PricingCategoryEnum::INTERNET;
$body_documentPacketData_scarecrowApplication_cardPricing_cardCharges = [];

$body_documentPacketData_scarecrowApplication_cardPricing_cardCharges_0_cardType = Models\CardTypeEnum::UK_DOMESTIC_MAESTRO;
$body_documentPacketData_scarecrowApplication_cardPricing_cardCharges[0] = new Models\CardCharge(
    $body_documentPacketData_scarecrowApplication_cardPricing_cardCharges_0_cardType
);

$body_documentPacketData_scarecrowApplication_cardPricing = new Models\CardPricing(
    $body_documentPacketData_scarecrowApplication_cardPricing_pricingMethod,
    $body_documentPacketData_scarecrowApplication_cardPricing_pricingCategory,
    $body_documentPacketData_scarecrowApplication_cardPricing_cardCharges
);
$body_documentPacketData_scarecrowApplication_parentEntity = 'parentEntity4';
$body_documentPacketData_scarecrowApplication = new Models\ScarecrowApplication(
    $body_documentPacketData_scarecrowApplication_clientId,
    $body_documentPacketData_scarecrowApplication_uniqueId,
    $body_documentPacketData_scarecrowApplication_country,
    $body_documentPacketData_scarecrowApplication_principal,
    $body_documentPacketData_scarecrowApplication_businessInfo,
    $body_documentPacketData_scarecrowApplication_financialInfo,
    $body_documentPacketData_scarecrowApplication_salesRepCode,
    $body_documentPacketData_scarecrowApplication_contact,
    $body_documentPacketData_scarecrowApplication_bankAccounts,
    $body_documentPacketData_scarecrowApplication_cardPricing,
    $body_documentPacketData_scarecrowApplication_parentEntity
);
$body_documentPacketData_language = 'language2';
$body_documentPacketData_vendorInfo = new Models\ProviderInfo;
$body_documentPacketData_bankAccountDetailsMap = [];

$body_documentPacketData_bankAccountDetailsMap[''] = new Models\BankAccountAdditionalInfo;

$body_documentPacketData_bankAccountDetailsMap[''] = new Models\BankAccountAdditionalInfo;

$body_documentPacketData_displayedCurrency = 'displayedCurrency8';
$body_documentPacketData = new Models\DocumentPacketData(
    $body_documentPacketData_scarecrowApplication,
    $body_documentPacketData_language,
    $body_documentPacketData_vendorInfo,
    $body_documentPacketData_bankAccountDetailsMap,
    $body_documentPacketData_displayedCurrency
);
$body = new Models\AppendGroupDocumentPacketRequest(
    $body_groupDocumentPacketId,
    $body_profileCode,
    $body_signers,
    $body_documentPacketData
);

$result = $sATIDAPIController->appendGroupDocumentPacket($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Create Document Packet

Create a document packet

```php
function createDocumentPacket(CreateDocumentPacketRequest $body): CreateDocumentPacketResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateDocumentPacketRequest`](../../doc/models/create-document-packet-request.md) | Body, Required | - |

## Response Type

[`CreateDocumentPacketResponse`](../../doc/models/create-document-packet-response.md)

## Example Usage

```php
$body_profileCode = 'TEST';
$body_signers = [];

$body_signers_0_signerId = 'signerId4';
$body_signers_0_signer_firstName = 'John';
$body_signers_0_signer_lastName = 'Doe';
$body_signers_0_signer = new Models\Name(
    $body_signers_0_signer_firstName,
    $body_signers_0_signer_lastName
);
$body_signers_0_principal = false;
$body_signers[0] = new Models\Signer(
    $body_signers_0_signerId,
    $body_signers_0_signer,
    $body_signers_0_principal
);

$body_signers_1_signerId = 'signerId5';
$body_signers_1_signer_firstName = 'John';
$body_signers_1_signer_lastName = 'Doe';
$body_signers_1_signer = new Models\Name(
    $body_signers_1_signer_firstName,
    $body_signers_1_signer_lastName
);
$body_signers_1_principal = true;
$body_signers[1] = new Models\Signer(
    $body_signers_1_signerId,
    $body_signers_1_signer,
    $body_signers_1_principal
);

$body_signers_2_signerId = 'signerId6';
$body_signers_2_signer_firstName = 'John';
$body_signers_2_signer_lastName = 'Doe';
$body_signers_2_signer = new Models\Name(
    $body_signers_2_signer_firstName,
    $body_signers_2_signer_lastName
);
$body_signers_2_principal = false;
$body_signers[2] = new Models\Signer(
    $body_signers_2_signerId,
    $body_signers_2_signer,
    $body_signers_2_principal
);

$body_documentPacketData_scarecrowApplication_clientId = 'IDNA';
$body_documentPacketData_scarecrowApplication_uniqueId = 'AcmeCorp1572566399123';
$body_documentPacketData_scarecrowApplication_country = 'USA';
$body_documentPacketData_scarecrowApplication_principal_name_firstName = 'John';
$body_documentPacketData_scarecrowApplication_principal_name_lastName = 'Doe';
$body_documentPacketData_scarecrowApplication_principal_name = new Models\Name(
    $body_documentPacketData_scarecrowApplication_principal_name_firstName,
    $body_documentPacketData_scarecrowApplication_principal_name_lastName
);
$body_documentPacketData_scarecrowApplication_principal_positions = ['key0' => false, 'key1' => true, 'key2' => false];
$body_documentPacketData_scarecrowApplication_principal = new Models\Person(
    $body_documentPacketData_scarecrowApplication_principal_name,
    $body_documentPacketData_scarecrowApplication_principal_positions
);
$body_documentPacketData_scarecrowApplication_businessInfo_dbaName = 'Grimm\'s Bookstore';
$body_documentPacketData_scarecrowApplication_businessInfo_dbaNameExtended = 'Grimm\'s Fairytales and Other Stories Bookstore';
$body_documentPacketData_scarecrowApplication_businessInfo_businessAddress_streetName = 'Baker Street';
$body_documentPacketData_scarecrowApplication_businessInfo_businessAddress_city = 'Atlanta';
$body_documentPacketData_scarecrowApplication_businessInfo_businessAddress_country = 'USA';
$body_documentPacketData_scarecrowApplication_businessInfo_businessAddress = new Models\Address(
    $body_documentPacketData_scarecrowApplication_businessInfo_businessAddress_streetName,
    $body_documentPacketData_scarecrowApplication_businessInfo_businessAddress_city,
    $body_documentPacketData_scarecrowApplication_businessInfo_businessAddress_country
);
$body_documentPacketData_scarecrowApplication_businessInfo_legalName = 'Barkers Dog Bakery';
$body_documentPacketData_scarecrowApplication_businessInfo_legalNameExtended = 'Baking Better Biscuits for Your Favorite Barkers Dog Bakery LLC';
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses = [];

$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__streetName = null;
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__city = null;
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__country = null;
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses[''] = new Models\Address(
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__streetName,
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__city,
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__country
);

$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__streetName = null;
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__city = null;
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__country = null;
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses[''] = new Models\Address(
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__streetName,
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__city,
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__country
);

$body_documentPacketData_scarecrowApplication_businessInfo_ownershipType = Models\OwnershipTypeEnum::LIMITED_PARTNERSHIP;
$body_documentPacketData_scarecrowApplication_businessInfo_productDescription = 'Bakeries';
$body_documentPacketData_scarecrowApplication_businessInfo_mccCode = '7399E';
$body_documentPacketData_scarecrowApplication_businessInfo_establishmentYear = '2005';
$body_documentPacketData_scarecrowApplication_businessInfo_currentOwnershipYears = '3';
$body_documentPacketData_scarecrowApplication_businessInfo_currentOwnershipMonths = '6';
$body_documentPacketData_scarecrowApplication_businessInfo_communicationLanguage = 'en';
$body_documentPacketData_scarecrowApplication_businessInfo_posLanguage = 'en';
$body_documentPacketData_scarecrowApplication_businessInfo = new Models\BusinessInfo(
    $body_documentPacketData_scarecrowApplication_businessInfo_dbaName,
    $body_documentPacketData_scarecrowApplication_businessInfo_dbaNameExtended,
    $body_documentPacketData_scarecrowApplication_businessInfo_businessAddress,
    $body_documentPacketData_scarecrowApplication_businessInfo_legalName,
    $body_documentPacketData_scarecrowApplication_businessInfo_legalNameExtended,
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses,
    $body_documentPacketData_scarecrowApplication_businessInfo_ownershipType,
    $body_documentPacketData_scarecrowApplication_businessInfo_productDescription,
    $body_documentPacketData_scarecrowApplication_businessInfo_mccCode,
    $body_documentPacketData_scarecrowApplication_businessInfo_establishmentYear,
    $body_documentPacketData_scarecrowApplication_businessInfo_currentOwnershipYears,
    $body_documentPacketData_scarecrowApplication_businessInfo_currentOwnershipMonths,
    $body_documentPacketData_scarecrowApplication_businessInfo_communicationLanguage,
    $body_documentPacketData_scarecrowApplication_businessInfo_posLanguage
);
$body_documentPacketData_scarecrowApplication_financialInfo_avgSaleAmount = '125';
$body_documentPacketData_scarecrowApplication_financialInfo_monthlyCardSales = '1000';
$body_documentPacketData_scarecrowApplication_financialInfo_cardPresentAcceptancePercent = '100';
$body_documentPacketData_scarecrowApplication_financialInfo_internetAcceptancePercent = '0';
$body_documentPacketData_scarecrowApplication_financialInfo_motoAcceptancePercent = '0';
$body_documentPacketData_scarecrowApplication_financialInfo = new Models\FinancialInfo(
    $body_documentPacketData_scarecrowApplication_financialInfo_avgSaleAmount,
    $body_documentPacketData_scarecrowApplication_financialInfo_monthlyCardSales,
    $body_documentPacketData_scarecrowApplication_financialInfo_cardPresentAcceptancePercent,
    $body_documentPacketData_scarecrowApplication_financialInfo_internetAcceptancePercent,
    $body_documentPacketData_scarecrowApplication_financialInfo_motoAcceptancePercent
);
$body_documentPacketData_scarecrowApplication_salesRepCode = '12345';
$body_documentPacketData_scarecrowApplication_contact_name_firstName = 'John';
$body_documentPacketData_scarecrowApplication_contact_name_lastName = 'Doe';
$body_documentPacketData_scarecrowApplication_contact_name = new Models\Name(
    $body_documentPacketData_scarecrowApplication_contact_name_firstName,
    $body_documentPacketData_scarecrowApplication_contact_name_lastName
);
$body_documentPacketData_scarecrowApplication_contact_positions = ['key0' => false, 'key1' => true];
$body_documentPacketData_scarecrowApplication_contact = new Models\Person(
    $body_documentPacketData_scarecrowApplication_contact_name,
    $body_documentPacketData_scarecrowApplication_contact_positions
);
$body_documentPacketData_scarecrowApplication_bankAccounts = [];

$body_documentPacketData_scarecrowApplication_bankAccounts__fundingMethod = envrr;
$body_documentPacketData_scarecrowApplication_bankAccounts__accountNumber = null;
$body_documentPacketData_scarecrowApplication_bankAccounts__sortCode = null;
$body_documentPacketData_scarecrowApplication_bankAccounts[''] = new Models\BankingInfo(
    $body_documentPacketData_scarecrowApplication_bankAccounts__fundingMethod,
    $body_documentPacketData_scarecrowApplication_bankAccounts__accountNumber,
    $body_documentPacketData_scarecrowApplication_bankAccounts__sortCode
);

$body_documentPacketData_scarecrowApplication_cardPricing_pricingMethod = Models\PricingMethodEnum::TIERED_PRICING;
$body_documentPacketData_scarecrowApplication_cardPricing_pricingCategory = Models\PricingCategoryEnum::INTERNET;
$body_documentPacketData_scarecrowApplication_cardPricing_cardCharges = [];

$body_documentPacketData_scarecrowApplication_cardPricing_cardCharges_0_cardType = Models\CardTypeEnum::UK_DOMESTIC_MAESTRO;
$body_documentPacketData_scarecrowApplication_cardPricing_cardCharges[0] = new Models\CardCharge(
    $body_documentPacketData_scarecrowApplication_cardPricing_cardCharges_0_cardType
);

$body_documentPacketData_scarecrowApplication_cardPricing = new Models\CardPricing(
    $body_documentPacketData_scarecrowApplication_cardPricing_pricingMethod,
    $body_documentPacketData_scarecrowApplication_cardPricing_pricingCategory,
    $body_documentPacketData_scarecrowApplication_cardPricing_cardCharges
);
$body_documentPacketData_scarecrowApplication_parentEntity = 'parentEntity4';
$body_documentPacketData_scarecrowApplication = new Models\ScarecrowApplication(
    $body_documentPacketData_scarecrowApplication_clientId,
    $body_documentPacketData_scarecrowApplication_uniqueId,
    $body_documentPacketData_scarecrowApplication_country,
    $body_documentPacketData_scarecrowApplication_principal,
    $body_documentPacketData_scarecrowApplication_businessInfo,
    $body_documentPacketData_scarecrowApplication_financialInfo,
    $body_documentPacketData_scarecrowApplication_salesRepCode,
    $body_documentPacketData_scarecrowApplication_contact,
    $body_documentPacketData_scarecrowApplication_bankAccounts,
    $body_documentPacketData_scarecrowApplication_cardPricing,
    $body_documentPacketData_scarecrowApplication_parentEntity
);
$body_documentPacketData_language = 'language2';
$body_documentPacketData_vendorInfo = new Models\ProviderInfo;
$body_documentPacketData_bankAccountDetailsMap = [];

$body_documentPacketData_bankAccountDetailsMap[''] = new Models\BankAccountAdditionalInfo;

$body_documentPacketData_bankAccountDetailsMap[''] = new Models\BankAccountAdditionalInfo;

$body_documentPacketData_displayedCurrency = 'displayedCurrency8';
$body_documentPacketData = new Models\DocumentPacketData(
    $body_documentPacketData_scarecrowApplication,
    $body_documentPacketData_language,
    $body_documentPacketData_vendorInfo,
    $body_documentPacketData_bankAccountDetailsMap,
    $body_documentPacketData_displayedCurrency
);
$body = new Models\CreateDocumentPacketRequest(
    $body_profileCode,
    $body_signers,
    $body_documentPacketData
);

$result = $sATIDAPIController->createDocumentPacket($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Credit Check

Credit Check

```php
function creditCheck(int $versionNumber, ScarecrowApplication $body): CreditCheckResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `versionNumber` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-4]` |
| `body` | [`ScarecrowApplication`](../../doc/models/scarecrow-application.md) | Body, Required | - |

## Response Type

[`CreditCheckResponse`](../../doc/models/credit-check-response.md)

## Example Usage

```php
$versionNumber = 66;
$body_clientId = 'IDNA';
$body_uniqueId = 'AcmeCorp1572566399123';
$body_country = 'USA';
$body_principal_name_firstName = 'John';
$body_principal_name_lastName = 'Doe';
$body_principal_name = new Models\Name(
    $body_principal_name_firstName,
    $body_principal_name_lastName
);
$body_principal_positions = ['key0' => false];
$body_principal = new Models\Person(
    $body_principal_name,
    $body_principal_positions
);
$body_businessInfo_dbaName = 'Grimm\'s Bookstore';
$body_businessInfo_dbaNameExtended = 'Grimm\'s Fairytales and Other Stories Bookstore';
$body_businessInfo_businessAddress_streetName = 'Baker Street';
$body_businessInfo_businessAddress_city = 'Atlanta';
$body_businessInfo_businessAddress_country = 'USA';
$body_businessInfo_businessAddress = new Models\Address(
    $body_businessInfo_businessAddress_streetName,
    $body_businessInfo_businessAddress_city,
    $body_businessInfo_businessAddress_country
);
$body_businessInfo_legalName = 'Barkers Dog Bakery';
$body_businessInfo_legalNameExtended = 'Baking Better Biscuits for Your Favorite Barkers Dog Bakery LLC';
$body_businessInfo_additionalAddresses = [];

$body_businessInfo_additionalAddresses__streetName = null;
$body_businessInfo_additionalAddresses__city = null;
$body_businessInfo_additionalAddresses__country = null;
$body_businessInfo_additionalAddresses[''] = new Models\Address(
    $body_businessInfo_additionalAddresses__streetName,
    $body_businessInfo_additionalAddresses__city,
    $body_businessInfo_additionalAddresses__country
);

$body_businessInfo_additionalAddresses__streetName = null;
$body_businessInfo_additionalAddresses__city = null;
$body_businessInfo_additionalAddresses__country = null;
$body_businessInfo_additionalAddresses[''] = new Models\Address(
    $body_businessInfo_additionalAddresses__streetName,
    $body_businessInfo_additionalAddresses__city,
    $body_businessInfo_additionalAddresses__country
);

$body_businessInfo_additionalAddresses__streetName = null;
$body_businessInfo_additionalAddresses__city = null;
$body_businessInfo_additionalAddresses__country = null;
$body_businessInfo_additionalAddresses[''] = new Models\Address(
    $body_businessInfo_additionalAddresses__streetName,
    $body_businessInfo_additionalAddresses__city,
    $body_businessInfo_additionalAddresses__country
);

$body_businessInfo_ownershipType = Models\OwnershipTypeEnum::PARTNERSHIP_LIMITED_BY_SHARES;
$body_businessInfo_productDescription = 'Bakeries';
$body_businessInfo_mccCode = '7399E';
$body_businessInfo_establishmentYear = '2005';
$body_businessInfo_currentOwnershipYears = '3';
$body_businessInfo_currentOwnershipMonths = '6';
$body_businessInfo_communicationLanguage = 'en';
$body_businessInfo_posLanguage = 'en';
$body_businessInfo = new Models\BusinessInfo(
    $body_businessInfo_dbaName,
    $body_businessInfo_dbaNameExtended,
    $body_businessInfo_businessAddress,
    $body_businessInfo_legalName,
    $body_businessInfo_legalNameExtended,
    $body_businessInfo_additionalAddresses,
    $body_businessInfo_ownershipType,
    $body_businessInfo_productDescription,
    $body_businessInfo_mccCode,
    $body_businessInfo_establishmentYear,
    $body_businessInfo_currentOwnershipYears,
    $body_businessInfo_currentOwnershipMonths,
    $body_businessInfo_communicationLanguage,
    $body_businessInfo_posLanguage
);
$body_financialInfo_avgSaleAmount = '125';
$body_financialInfo_monthlyCardSales = '1000';
$body_financialInfo_cardPresentAcceptancePercent = '100';
$body_financialInfo_internetAcceptancePercent = '0';
$body_financialInfo_motoAcceptancePercent = '0';
$body_financialInfo = new Models\FinancialInfo(
    $body_financialInfo_avgSaleAmount,
    $body_financialInfo_monthlyCardSales,
    $body_financialInfo_cardPresentAcceptancePercent,
    $body_financialInfo_internetAcceptancePercent,
    $body_financialInfo_motoAcceptancePercent
);
$body_salesRepCode = '12345';
$body_contact_name_firstName = 'John';
$body_contact_name_lastName = 'Doe';
$body_contact_name = new Models\Name(
    $body_contact_name_firstName,
    $body_contact_name_lastName
);
$body_contact_positions = ['key0' => false];
$body_contact = new Models\Person(
    $body_contact_name,
    $body_contact_positions
);
$body_bankAccounts = [];

$body_bankAccounts__fundingMethod = envrr;
$body_bankAccounts__accountNumber = null;
$body_bankAccounts__sortCode = null;
$body_bankAccounts[''] = new Models\BankingInfo(
    $body_bankAccounts__fundingMethod,
    $body_bankAccounts__accountNumber,
    $body_bankAccounts__sortCode
);

$body_bankAccounts__fundingMethod = envrr;
$body_bankAccounts__accountNumber = null;
$body_bankAccounts__sortCode = null;
$body_bankAccounts[''] = new Models\BankingInfo(
    $body_bankAccounts__fundingMethod,
    $body_bankAccounts__accountNumber,
    $body_bankAccounts__sortCode
);

$body_bankAccounts__fundingMethod = envrr;
$body_bankAccounts__accountNumber = null;
$body_bankAccounts__sortCode = null;
$body_bankAccounts[''] = new Models\BankingInfo(
    $body_bankAccounts__fundingMethod,
    $body_bankAccounts__accountNumber,
    $body_bankAccounts__sortCode
);

$body_cardPricing_pricingMethod = Models\PricingMethodEnum::CLEAR_AND_SIMPLE;
$body_cardPricing_pricingCategory = Models\PricingCategoryEnum::RETAIL;
$body_cardPricing_cardCharges = [];

$body_cardPricing_cardCharges_0_cardType = Models\CardTypeEnum::VISA_DEBIT;
$body_cardPricing_cardCharges[0] = new Models\CardCharge(
    $body_cardPricing_cardCharges_0_cardType
);

$body_cardPricing_cardCharges_1_cardType = Models\CardTypeEnum::VPAY;
$body_cardPricing_cardCharges[1] = new Models\CardCharge(
    $body_cardPricing_cardCharges_1_cardType
);

$body_cardPricing = new Models\CardPricing(
    $body_cardPricing_pricingMethod,
    $body_cardPricing_pricingCategory,
    $body_cardPricing_cardCharges
);
$body_parentEntity = 'parentEntity8';
$body = new Models\ScarecrowApplication(
    $body_clientId,
    $body_uniqueId,
    $body_country,
    $body_principal,
    $body_businessInfo,
    $body_financialInfo,
    $body_salesRepCode,
    $body_contact,
    $body_bankAccounts,
    $body_cardPricing,
    $body_parentEntity
);

$result = $sATIDAPIController->creditCheck($versionNumber, $body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Update Document Packet Data

Update document packet

```php
function updateDocumentPacketData(UpdateDocumentPacketDataRequest $body): UpdateDocumentPacketDataResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UpdateDocumentPacketDataRequest`](../../doc/models/update-document-packet-data-request.md) | Body, Required | - |

## Response Type

[`UpdateDocumentPacketDataResponse`](../../doc/models/update-document-packet-data-response.md)

## Example Usage

```php
$body_documentPacketId = 'documentPacketId2';
$body_documentPacketData_scarecrowApplication_clientId = 'IDNA';
$body_documentPacketData_scarecrowApplication_uniqueId = 'AcmeCorp1572566399123';
$body_documentPacketData_scarecrowApplication_country = 'USA';
$body_documentPacketData_scarecrowApplication_principal_name_firstName = 'John';
$body_documentPacketData_scarecrowApplication_principal_name_lastName = 'Doe';
$body_documentPacketData_scarecrowApplication_principal_name = new Models\Name(
    $body_documentPacketData_scarecrowApplication_principal_name_firstName,
    $body_documentPacketData_scarecrowApplication_principal_name_lastName
);
$body_documentPacketData_scarecrowApplication_principal_positions = ['key0' => false, 'key1' => true, 'key2' => false];
$body_documentPacketData_scarecrowApplication_principal = new Models\Person(
    $body_documentPacketData_scarecrowApplication_principal_name,
    $body_documentPacketData_scarecrowApplication_principal_positions
);
$body_documentPacketData_scarecrowApplication_businessInfo_dbaName = 'Grimm\'s Bookstore';
$body_documentPacketData_scarecrowApplication_businessInfo_dbaNameExtended = 'Grimm\'s Fairytales and Other Stories Bookstore';
$body_documentPacketData_scarecrowApplication_businessInfo_businessAddress_streetName = 'Baker Street';
$body_documentPacketData_scarecrowApplication_businessInfo_businessAddress_city = 'Atlanta';
$body_documentPacketData_scarecrowApplication_businessInfo_businessAddress_country = 'USA';
$body_documentPacketData_scarecrowApplication_businessInfo_businessAddress = new Models\Address(
    $body_documentPacketData_scarecrowApplication_businessInfo_businessAddress_streetName,
    $body_documentPacketData_scarecrowApplication_businessInfo_businessAddress_city,
    $body_documentPacketData_scarecrowApplication_businessInfo_businessAddress_country
);
$body_documentPacketData_scarecrowApplication_businessInfo_legalName = 'Barkers Dog Bakery';
$body_documentPacketData_scarecrowApplication_businessInfo_legalNameExtended = 'Baking Better Biscuits for Your Favorite Barkers Dog Bakery LLC';
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses = [];

$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__streetName = null;
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__city = null;
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__country = null;
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses[''] = new Models\Address(
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__streetName,
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__city,
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__country
);

$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__streetName = null;
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__city = null;
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__country = null;
$body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses[''] = new Models\Address(
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__streetName,
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__city,
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses__country
);

$body_documentPacketData_scarecrowApplication_businessInfo_ownershipType = Models\OwnershipTypeEnum::LIMITED_PARTNERSHIP;
$body_documentPacketData_scarecrowApplication_businessInfo_productDescription = 'Bakeries';
$body_documentPacketData_scarecrowApplication_businessInfo_mccCode = '7399E';
$body_documentPacketData_scarecrowApplication_businessInfo_establishmentYear = '2005';
$body_documentPacketData_scarecrowApplication_businessInfo_currentOwnershipYears = '3';
$body_documentPacketData_scarecrowApplication_businessInfo_currentOwnershipMonths = '6';
$body_documentPacketData_scarecrowApplication_businessInfo_communicationLanguage = 'en';
$body_documentPacketData_scarecrowApplication_businessInfo_posLanguage = 'en';
$body_documentPacketData_scarecrowApplication_businessInfo = new Models\BusinessInfo(
    $body_documentPacketData_scarecrowApplication_businessInfo_dbaName,
    $body_documentPacketData_scarecrowApplication_businessInfo_dbaNameExtended,
    $body_documentPacketData_scarecrowApplication_businessInfo_businessAddress,
    $body_documentPacketData_scarecrowApplication_businessInfo_legalName,
    $body_documentPacketData_scarecrowApplication_businessInfo_legalNameExtended,
    $body_documentPacketData_scarecrowApplication_businessInfo_additionalAddresses,
    $body_documentPacketData_scarecrowApplication_businessInfo_ownershipType,
    $body_documentPacketData_scarecrowApplication_businessInfo_productDescription,
    $body_documentPacketData_scarecrowApplication_businessInfo_mccCode,
    $body_documentPacketData_scarecrowApplication_businessInfo_establishmentYear,
    $body_documentPacketData_scarecrowApplication_businessInfo_currentOwnershipYears,
    $body_documentPacketData_scarecrowApplication_businessInfo_currentOwnershipMonths,
    $body_documentPacketData_scarecrowApplication_businessInfo_communicationLanguage,
    $body_documentPacketData_scarecrowApplication_businessInfo_posLanguage
);
$body_documentPacketData_scarecrowApplication_financialInfo_avgSaleAmount = '125';
$body_documentPacketData_scarecrowApplication_financialInfo_monthlyCardSales = '1000';
$body_documentPacketData_scarecrowApplication_financialInfo_cardPresentAcceptancePercent = '100';
$body_documentPacketData_scarecrowApplication_financialInfo_internetAcceptancePercent = '0';
$body_documentPacketData_scarecrowApplication_financialInfo_motoAcceptancePercent = '0';
$body_documentPacketData_scarecrowApplication_financialInfo = new Models\FinancialInfo(
    $body_documentPacketData_scarecrowApplication_financialInfo_avgSaleAmount,
    $body_documentPacketData_scarecrowApplication_financialInfo_monthlyCardSales,
    $body_documentPacketData_scarecrowApplication_financialInfo_cardPresentAcceptancePercent,
    $body_documentPacketData_scarecrowApplication_financialInfo_internetAcceptancePercent,
    $body_documentPacketData_scarecrowApplication_financialInfo_motoAcceptancePercent
);
$body_documentPacketData_scarecrowApplication_salesRepCode = '12345';
$body_documentPacketData_scarecrowApplication_contact_name_firstName = 'John';
$body_documentPacketData_scarecrowApplication_contact_name_lastName = 'Doe';
$body_documentPacketData_scarecrowApplication_contact_name = new Models\Name(
    $body_documentPacketData_scarecrowApplication_contact_name_firstName,
    $body_documentPacketData_scarecrowApplication_contact_name_lastName
);
$body_documentPacketData_scarecrowApplication_contact_positions = ['key0' => false, 'key1' => true];
$body_documentPacketData_scarecrowApplication_contact = new Models\Person(
    $body_documentPacketData_scarecrowApplication_contact_name,
    $body_documentPacketData_scarecrowApplication_contact_positions
);
$body_documentPacketData_scarecrowApplication_bankAccounts = [];

$body_documentPacketData_scarecrowApplication_bankAccounts__fundingMethod = envrr;
$body_documentPacketData_scarecrowApplication_bankAccounts__accountNumber = null;
$body_documentPacketData_scarecrowApplication_bankAccounts__sortCode = null;
$body_documentPacketData_scarecrowApplication_bankAccounts[''] = new Models\BankingInfo(
    $body_documentPacketData_scarecrowApplication_bankAccounts__fundingMethod,
    $body_documentPacketData_scarecrowApplication_bankAccounts__accountNumber,
    $body_documentPacketData_scarecrowApplication_bankAccounts__sortCode
);

$body_documentPacketData_scarecrowApplication_cardPricing_pricingMethod = Models\PricingMethodEnum::TIERED_PRICING;
$body_documentPacketData_scarecrowApplication_cardPricing_pricingCategory = Models\PricingCategoryEnum::INTERNET;
$body_documentPacketData_scarecrowApplication_cardPricing_cardCharges = [];

$body_documentPacketData_scarecrowApplication_cardPricing_cardCharges_0_cardType = Models\CardTypeEnum::UK_DOMESTIC_MAESTRO;
$body_documentPacketData_scarecrowApplication_cardPricing_cardCharges[0] = new Models\CardCharge(
    $body_documentPacketData_scarecrowApplication_cardPricing_cardCharges_0_cardType
);

$body_documentPacketData_scarecrowApplication_cardPricing = new Models\CardPricing(
    $body_documentPacketData_scarecrowApplication_cardPricing_pricingMethod,
    $body_documentPacketData_scarecrowApplication_cardPricing_pricingCategory,
    $body_documentPacketData_scarecrowApplication_cardPricing_cardCharges
);
$body_documentPacketData_scarecrowApplication_parentEntity = 'parentEntity4';
$body_documentPacketData_scarecrowApplication = new Models\ScarecrowApplication(
    $body_documentPacketData_scarecrowApplication_clientId,
    $body_documentPacketData_scarecrowApplication_uniqueId,
    $body_documentPacketData_scarecrowApplication_country,
    $body_documentPacketData_scarecrowApplication_principal,
    $body_documentPacketData_scarecrowApplication_businessInfo,
    $body_documentPacketData_scarecrowApplication_financialInfo,
    $body_documentPacketData_scarecrowApplication_salesRepCode,
    $body_documentPacketData_scarecrowApplication_contact,
    $body_documentPacketData_scarecrowApplication_bankAccounts,
    $body_documentPacketData_scarecrowApplication_cardPricing,
    $body_documentPacketData_scarecrowApplication_parentEntity
);
$body_documentPacketData_language = 'language2';
$body_documentPacketData_vendorInfo = new Models\ProviderInfo;
$body_documentPacketData_bankAccountDetailsMap = [];

$body_documentPacketData_bankAccountDetailsMap[''] = new Models\BankAccountAdditionalInfo;

$body_documentPacketData_bankAccountDetailsMap[''] = new Models\BankAccountAdditionalInfo;

$body_documentPacketData_displayedCurrency = 'displayedCurrency8';
$body_documentPacketData = new Models\DocumentPacketData(
    $body_documentPacketData_scarecrowApplication,
    $body_documentPacketData_language,
    $body_documentPacketData_vendorInfo,
    $body_documentPacketData_bankAccountDetailsMap,
    $body_documentPacketData_displayedCurrency
);
$body = new Models\UpdateDocumentPacketDataRequest(
    $body_documentPacketId,
    $body_documentPacketData
);

$result = $sATIDAPIController->updateDocumentPacketData($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Check Document Signing Status

Check the signing status of one or more signer of a packet

```php
function checkDocumentSigningStatus(CheckDocumentSigningStatusRequest $body): CheckDocumentSigningStatusResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CheckDocumentSigningStatusRequest`](../../doc/models/check-document-signing-status-request.md) | Body, Required | - |

## Response Type

[`CheckDocumentSigningStatusResponse`](../../doc/models/check-document-signing-status-response.md)

## Example Usage

```php
$body = new Models\CheckDocumentSigningStatusRequest;

$result = $sATIDAPIController->checkDocumentSigningStatus($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Delete Document Packet

Delete a Document Packet

```php
function deleteDocumentPacket(DeleteDocumentPacketRequest $body): DeleteDocumentPacketResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeleteDocumentPacketRequest`](../../doc/models/delete-document-packet-request.md) | Body, Required | - |

## Response Type

[`DeleteDocumentPacketResponse`](../../doc/models/delete-document-packet-response.md)

## Example Usage

```php
$body = new Models\DeleteDocumentPacketRequest;

$result = $sATIDAPIController->deleteDocumentPacket($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Delete Group Document Packet

Delete Group Document Packet

```php
function deleteGroupDocumentPacket(DeleteGroupDocumentPacketRequest $body): DeleteGroupDocumentPacketResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeleteGroupDocumentPacketRequest`](../../doc/models/delete-group-document-packet-request.md) | Body, Required | - |

## Response Type

[`DeleteGroupDocumentPacketResponse`](../../doc/models/delete-group-document-packet-response.md)

## Example Usage

```php
$body = new Models\DeleteGroupDocumentPacketRequest;

$result = $sATIDAPIController->deleteGroupDocumentPacket($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Update Document Packet

Update Document Packet

```php
function updateDocumentPacket(UpdateDocumentPacketRequest $body): UpdateDocumentPacketResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UpdateDocumentPacketRequest`](../../doc/models/update-document-packet-request.md) | Body, Required | - |

## Response Type

[`UpdateDocumentPacketResponse`](../../doc/models/update-document-packet-response.md)

## Example Usage

```php
$body_documentPacketId = 'documentPacketId2';
$body = new Models\UpdateDocumentPacketRequest(
    $body_documentPacketId
);

$result = $sATIDAPIController->updateDocumentPacket($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Execute Group Document Packet

Execute Document Packet

```php
function executeGroupDocumentPacket(ExecuteGroupDocumentPacketRequest $body): ExecuteGroupDocumentPacketResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ExecuteGroupDocumentPacketRequest`](../../doc/models/execute-group-document-packet-request.md) | Body, Required | - |

## Response Type

[`ExecuteGroupDocumentPacketResponse`](../../doc/models/execute-group-document-packet-response.md)

## Example Usage

```php
$body_groupDocumentPacketId = 'groupDocumentPacketId4';
$body = new Models\ExecuteGroupDocumentPacketRequest(
    $body_groupDocumentPacketId
);

$result = $sATIDAPIController->executeGroupDocumentPacket($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Get Unsigned Document Content

Get unsigned document packet singular document

```php
function getUnsignedDocumentContent(GetUnsignedDocumentRequest $body): GetDocumentResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetUnsignedDocumentRequest`](../../doc/models/get-unsigned-document-request.md) | Body, Required | - |

## Response Type

[`GetDocumentResponse`](../../doc/models/get-document-response.md)

## Example Usage

```php
$body = new Models\GetUnsignedDocumentRequest;

$result = $sATIDAPIController->getUnsignedDocumentContent($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |


# Get Unsigned Documents Packet Content

Get unsigned document packet full content

```php
function getUnsignedDocumentsPacketContent(GetUnsignedDocumentsPacketRequest $body): GetDocumentsResponse
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetUnsignedDocumentsPacketRequest`](../../doc/models/get-unsigned-documents-packet-request.md) | Body, Required | - |

## Response Type

[`GetDocumentsResponse`](../../doc/models/get-documents-response.md)

## Example Usage

```php
$body = new Models\GetUnsignedDocumentsPacketRequest;

$result = $sATIDAPIController->getUnsignedDocumentsPacketContent($body);
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `ApiException` |

