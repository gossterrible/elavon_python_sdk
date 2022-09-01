# SATIDAPI

```python
satidapi_controller = client.satidapi
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

```python
def upload_documents(self,
                    version_number,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version_number` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |
| `body` | [`UploadDocumentsRequestParams`](../../doc/models/upload-documents-request-params.md) | Body, Required | - |

## Response Type

[`UploadDocumentResponse`](../../doc/models/upload-document-response.md)

## Example Usage

```python
version_number = 66
body = UploadDocumentsRequestParams()
body.boarding_id = '2101491576'
body.client_id = 'IDNA'
body.unique_id = 'AcmeCorp1572566399123'
body.country = 'country0'
body.sales_rep_number = '12345'
body.image_document_data = ImageDocumentData()
body.image_document_data.doc_reference_number = 'docReferenceNumber4'
body.image_document_data.image_documents = []

body.image_document_data.image_documents.append(ImageDocument())
body.image_document_data.image_documents[0].image_id = 208
body.image_document_data.image_documents[0].image_type_code = 'APPLI'
body.image_document_data.image_documents[0].dba_name = 'Grimm\'s Bookstore'
body.image_document_data.image_documents[0].mime_type_code = MimeTypeCodeEnum.JPG
body.image_document_data.image_documents[0].image_content = ['imageContent4', 'imageContent5', 'imageContent6']

body.image_document_data.image_documents.append(ImageDocument())
body.image_document_data.image_documents[1].image_id = 209
body.image_document_data.image_documents[1].image_type_code = 'APPLI'
body.image_document_data.image_documents[1].dba_name = 'Grimm\'s Bookstore'
body.image_document_data.image_documents[1].mime_type_code = MimeTypeCodeEnum.PDF
body.image_document_data.image_documents[1].image_content = ['imageContent5']

body.image_document_data.image_documents.append(ImageDocument())
body.image_document_data.image_documents[2].image_id = 210
body.image_document_data.image_documents[2].image_type_code = 'APPLI'
body.image_document_data.image_documents[2].dba_name = 'Grimm\'s Bookstore'
body.image_document_data.image_documents[2].mime_type_code = MimeTypeCodeEnum.SVG
body.image_document_data.image_documents[2].image_content = ['imageContent6', 'imageContent7']


result = satid_api_controller.upload_documents(version_number, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Board

Boarding

```python
def board(self,
         version_number,
         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version_number` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-4]` |
| `body` | [`BoardingRequestParams`](../../doc/models/boarding-request-params.md) | Body, Required | - |

## Response Type

[`BoardingResponse`](../../doc/models/boarding-response.md)

## Example Usage

```python
version_number = 66
body = BoardingRequestParams()
body.scarecrow_application = ScarecrowApplication()
body.scarecrow_application.client_id = 'IDNA'
body.scarecrow_application.unique_id = 'AcmeCorp1572566399123'
body.scarecrow_application.country = 'USA'
body.scarecrow_application.principal = Person()
body.scarecrow_application.principal.name = Name()
body.scarecrow_application.principal.name.first_name = 'John'
body.scarecrow_application.principal.name.last_name = 'Doe'
body.scarecrow_application.principal.positions = {'key0' : False, 'key1' : True, 'key2' : False } 
body.scarecrow_application.business_info = BusinessInfo()
body.scarecrow_application.business_info.dba_name = 'Grimm\'s Bookstore'
body.scarecrow_application.business_info.dba_name_extended = 'Grimm\'s Fairytales and Other Stories Bookstore'
body.scarecrow_application.business_info.business_address = Address()
body.scarecrow_application.business_info.business_address.street_name = 'Baker Street'
body.scarecrow_application.business_info.business_address.city = 'Atlanta'
body.scarecrow_application.business_info.business_address.country = 'USA'
body.scarecrow_application.business_info.legal_name = 'Barkers Dog Bakery'
body.scarecrow_application.business_info.legal_name_extended = 'Baking Better Biscuits for Your Favorite Barkers Dog Bakery LLC'
body.scarecrow_application.business_info.additional_addresses = Address()
body.scarecrow_application.business_info.additional_addresses.street_name = None
body.scarecrow_application.business_info.additional_addresses.city = None
body.scarecrow_application.business_info.additional_addresses.country = None
body.scarecrow_application.business_info.ownership_type = OwnershipTypeEnum.PARTNERSHIP_LIMITED_BY_SHARES
body.scarecrow_application.business_info.product_description = 'Bakeries'
body.scarecrow_application.business_info.mcc_code = '7399E'
body.scarecrow_application.business_info.establishment_year = '2005'
body.scarecrow_application.business_info.current_ownership_years = '3'
body.scarecrow_application.business_info.current_ownership_months = '6'
body.scarecrow_application.business_info.communication_language = 'en'
body.scarecrow_application.business_info.pos_language = 'en'
body.scarecrow_application.financial_info = FinancialInfo()
body.scarecrow_application.financial_info.avg_sale_amount = '125'
body.scarecrow_application.financial_info.monthly_card_sales = '1000'
body.scarecrow_application.financial_info.card_present_acceptance_percent = '100'
body.scarecrow_application.financial_info.internet_acceptance_percent = '0'
body.scarecrow_application.financial_info.moto_acceptance_percent = '0'
body.scarecrow_application.sales_rep_code = '12345'
body.scarecrow_application.contact = Person()
body.scarecrow_application.contact.name = Name()
body.scarecrow_application.contact.name.first_name = 'John'
body.scarecrow_application.contact.name.last_name = 'Doe'
body.scarecrow_application.contact.positions = {'key0' : False, 'key1' : True } 
body.scarecrow_application.bank_accounts = BankingInfo()
body.scarecrow_application.bank_accounts.funding_method = envrr
body.scarecrow_application.bank_accounts.account_number = None
body.scarecrow_application.bank_accounts.sort_code = None
body.scarecrow_application.card_pricing = CardPricing()
body.scarecrow_application.card_pricing.pricing_method = PricingMethodEnum.ASSOCIATION
body.scarecrow_application.card_pricing.pricing_category = PricingCategoryEnum.MOTO
body.scarecrow_application.card_pricing.card_charges = []

body.scarecrow_application.card_pricing.card_charges.append(CardCharge())
body.scarecrow_application.card_pricing.card_charges[0].card_type = CardTypeEnum.VISA_DEBIT

body.scarecrow_application.parent_entity = 'parentEntity8'

result = satid_api_controller.board(version_number, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Postal Validate

Validate Postal Code

```python
def postal_validate(self,
                   version_number,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version_number` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |
| `body` | [`ValidateZipCodeRequest`](../../doc/models/validate-zip-code-request.md) | Body, Required | - |

## Response Type

[`ValidateZipCodeRequest`](../../doc/models/validate-zip-code-request.md)

## Example Usage

```python
version_number = 66
body = ValidateZipCodeRequest()
body.zip_code = '20330'
body.country = 'USA'

result = satid_api_controller.postal_validate(version_number, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Bank Validate

Validate Bank Account

```python
def bank_validate(self,
                 version_number,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version_number` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |
| `body` | [`BankingInfo`](../../doc/models/banking-info.md) | Body, Required | - |

## Response Type

[`VerifyBankAccountResponse`](../../doc/models/verify-bank-account-response.md)

## Example Usage

```python
version_number = 66
body = BankingInfo()
body.funding_method = FundingMethodEnum.NETCREDIT
body.account_number = '20581687'
body.sort_code = '121000248'

result = satid_api_controller.bank_validate(version_number, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Refresh Signer User Sessions

Refresh the session for signers of a document packet

```python
def refresh_signer_user_sessions(self,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RefreshSignerUsersSessionsRequest`](../../doc/models/refresh-signer-users-sessions-request.md) | Body, Required | - |

## Response Type

[`RefershSignerUserSessionsResponse`](../../doc/models/refersh-signer-user-sessions-response.md)

## Example Usage

```python
body = RefreshSignerUsersSessionsRequest()
body.document_packet_id = '42f441d0-0c23-468d-8319-f1e2af17dc15'
body.signer_ids = ['signerIds5', 'signerIds6', 'signerIds7']

result = satid_api_controller.refresh_signer_user_sessions(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Regenerate Packet Documents

Regenerate signed Packet Content in event of failure

```python
def regenerate_packet_documents(self,
                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RegenerateDocumentPacketRequest`](../../doc/models/regenerate-document-packet-request.md) | Body, Required | - |

## Response Type

[`Response`](../../doc/models/response.md)

## Example Usage

```python
body = RegenerateDocumentPacketRequest()
body.document_packet_id = 'documentPacketId2'

result = satid_api_controller.regenerate_packet_documents(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# List Packet Presented Documents

List Packet Documents to present to the user

```python
def list_packet_presented_documents(self,
                                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ListPacketDocumentsRequest`](../../doc/models/list-packet-documents-request.md) | Body, Required | - |

## Response Type

[`ListDocumentsResponse`](../../doc/models/list-documents-response.md)

## Example Usage

```python
body = ListPacketDocumentsRequest()

result = satid_api_controller.list_packet_presented_documents(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Get Signed Document Packet Content

Get signed document packet content

```python
def get_signed_document_packet_content(self,
                                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetSignedDocumentPacketRequest`](../../doc/models/get-signed-document-packet-request.md) | Body, Required | - |

## Response Type

[`GetDocumentsResponse`](../../doc/models/get-documents-response.md)

## Example Usage

```python
body = GetSignedDocumentPacketRequest()

result = satid_api_controller.get_signed_document_packet_content(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Generate Packet Documents

Trigger generation of document in packet for submission

```python
def generate_packet_documents(self,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GeneratePacketDocumentsRequest`](../../doc/models/generate-packet-documents-request.md) | Body, Required | - |

## Response Type

[`GeneratePacketDocumentsResponse`](../../doc/models/generate-packet-documents-response.md)

## Example Usage

```python
body = GeneratePacketDocumentsRequest()

result = satid_api_controller.generate_packet_documents(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Board Xsd Schema

Get Boarding Schema

```python
def board_xsd_schema(self,
                    version_number,
                    iso_3_country)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version_number` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-4]` |
| `iso_3_country` | `string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```python
version_number = 66
iso_3_country = 'iso3Country6'

result = satid_api_controller.board_xsd_schema(version_number, iso_3_country)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | successful operation | `APIException` |


# Credit Check Xsd Schema

Get Credit Check Schema

```python
def credit_check_xsd_schema(self,
                           version_number,
                           iso_3_country)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version_number` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-4]` |
| `iso_3_country` | `string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```python
version_number = 66
iso_3_country = 'iso3Country6'

result = satid_api_controller.credit_check_xsd_schema(version_number, iso_3_country)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | successful operation | `APIException` |


# Board Status Xsd Schema

Get Boarding Status Schema

```python
def board_status_xsd_schema(self,
                           version_number)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version_number` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |

## Response Type

`void`

## Example Usage

```python
version_number = 66

result = satid_api_controller.board_status_xsd_schema(version_number)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | successful operation | `APIException` |


# Upload Document Xsd Schema

Get Upload Documents Schema

```python
def upload_document_xsd_schema(self,
                              version_number)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version_number` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |

## Response Type

`void`

## Example Usage

```python
version_number = 66

result = satid_api_controller.upload_document_xsd_schema(version_number)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | successful operation | `APIException` |


# Post Code Xsd Schema

Get Postal Code Validation Schema

```python
def post_code_xsd_schema(self,
                        version_number)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version_number` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |

## Response Type

`void`

## Example Usage

```python
version_number = 66

result = satid_api_controller.post_code_xsd_schema(version_number)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | successful operation | `APIException` |


# Bank Xsd Schema

Get Bank Account Validation Schema

```python
def bank_xsd_schema(self,
                   version_number)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version_number` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |

## Response Type

`void`

## Example Usage

```python
version_number = 66

result = satid_api_controller.bank_xsd_schema(version_number)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | successful operation | `APIException` |


# Get Quiz Xsd Schema

Get Quiz Request Schema

```python
def get_quiz_xsd_schema(self,
                       version_number)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version_number` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |

## Response Type

`void`

## Example Usage

```python
version_number = 66

result = satid_api_controller.get_quiz_xsd_schema(version_number)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | successful operation | `APIException` |


# Answer Quiz Xsd Schema

Get Quiz Answer Schema

```python
def answer_quiz_xsd_schema(self,
                          version_number)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version_number` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |

## Response Type

`void`

## Example Usage

```python
version_number = 66

result = satid_api_controller.answer_quiz_xsd_schema(version_number)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | successful operation | `APIException` |


# Get Quiz

Request KYC Quiz

```python
def get_quiz(self,
            version_number,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version_number` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |
| `body` | [`GetQuizRequest`](../../doc/models/get-quiz-request.md) | Body, Required | - |

## Response Type

[`GetQuizResponse`](../../doc/models/get-quiz-response.md)

## Example Usage

```python
version_number = 66
body = GetQuizRequest()
body.principal = Person()
body.principal.name = Name()
body.principal.name.first_name = 'John'
body.principal.name.last_name = 'Doe'
body.principal.positions = {'key0' : False } 
body.business_address = Address()
body.business_address.street_name = 'Baker Street'
body.business_address.city = 'Atlanta'
body.business_address.country = 'USA'
body.language = 'en'

result = satid_api_controller.get_quiz(version_number, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Answer Quiz

Answer KYC Quiz

```python
def answer_quiz(self,
               version_number,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version_number` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |
| `body` | [`AnswerQuizRequest`](../../doc/models/answer-quiz-request.md) | Body, Required | - |

## Response Type

[`AnswerQuizResponse`](../../doc/models/answer-quiz-response.md)

## Example Usage

```python
version_number = 66
body = AnswerQuizRequest()
body.quiz_id = 162
body.transaction_key = 'transactionKey8'
body.quiz_answers = []

body.quiz_answers.append(QuizAnswer())
body.quiz_answers[0].question_number = 30
body.quiz_answers[0].answer_number = 20

body.quiz_answers.append(QuizAnswer())
body.quiz_answers[1].question_number = 31
body.quiz_answers[1].answer_number = 21


result = satid_api_controller.answer_quiz(version_number, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# List Presented Documents

List Documents to present to the user

```python
def list_presented_documents(self,
                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ListDocumentsRequest`](../../doc/models/list-documents-request.md) | Body, Required | - |

## Response Type

[`ListDocumentsResponse`](../../doc/models/list-documents-response.md)

## Example Usage

```python
body = ListDocumentsRequest()

result = satid_api_controller.list_presented_documents(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Get Presented Documents

Get all documents to present to the user

```python
def get_presented_documents(self,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetDocumentsRequest`](../../doc/models/get-documents-request.md) | Body, Required | - |

## Response Type

[`GetDocumentsResponse`](../../doc/models/get-documents-response.md)

## Example Usage

```python
body = GetDocumentsRequest()

result = satid_api_controller.get_presented_documents(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Board Status

Boarding Status

```python
def board_status(self,
                version_number,
                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version_number` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-2]` |
| `body` | [`BoardingStatusRequestParams`](../../doc/models/boarding-status-request-params.md) | Body, Required | - |

## Response Type

[`BoardingStatusResponse`](../../doc/models/boarding-status-response.md)

## Example Usage

```python
version_number = 66
body = BoardingStatusRequestParams()
body.client_id = 'IDNA'
body.unique_id = 'AcmeCorp1572566399123'
body.country = 'USA'
body.sales_rep_code = 'salesRepCode2'

result = satid_api_controller.board_status(version_number, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Get Terminal Ids

Get terminal ids and related information for MID

```python
def get_terminal_ids(self,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetTerminalIdsRequest`](../../doc/models/get-terminal-ids-request.md) | Body, Required | - |

## Response Type

[`GetTerminalIdsResponse`](../../doc/models/get-terminal-ids-response.md)

## Example Usage

```python
body = GetTerminalIdsRequest()

result = satid_api_controller.get_terminal_ids(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Create Group Document Packet

Create Group Document Packet

```python
def create_group_document_packet(self,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateGroupDocumentPacketRequest`](../../doc/models/create-group-document-packet-request.md) | Body, Required | - |

## Response Type

[`CreateGroupDocumentPacketResponse`](../../doc/models/create-group-document-packet-response.md)

## Example Usage

```python
body = CreateGroupDocumentPacketRequest()

result = satid_api_controller.create_group_document_packet(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Append Group Document Packet

Append to Group Document Packet

```python
def append_group_document_packet(self,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AppendGroupDocumentPacketRequest`](../../doc/models/append-group-document-packet-request.md) | Body, Required | - |

## Response Type

[`AppendGroupDocumentPacketResponse`](../../doc/models/append-group-document-packet-response.md)

## Example Usage

```python
body = AppendGroupDocumentPacketRequest()
body.group_document_packet_id = 'groupDocumentPacketId4'
body.profile_code = 'profileCode8'
body.signers = []

body.signers.append(Signer())
body.signers[0].signer_id = 'signerId4'
body.signers[0].signer = Name()
body.signers[0].signer.first_name = 'John'
body.signers[0].signer.last_name = 'Doe'
body.signers[0].principal = False

body.signers.append(Signer())
body.signers[1].signer_id = 'signerId5'
body.signers[1].signer = Name()
body.signers[1].signer.first_name = 'John'
body.signers[1].signer.last_name = 'Doe'
body.signers[1].principal = True

body.signers.append(Signer())
body.signers[2].signer_id = 'signerId6'
body.signers[2].signer = Name()
body.signers[2].signer.first_name = 'John'
body.signers[2].signer.last_name = 'Doe'
body.signers[2].principal = False

body.document_packet_data = DocumentPacketData()
body.document_packet_data.scarecrow_application = ScarecrowApplication()
body.document_packet_data.scarecrow_application.client_id = 'IDNA'
body.document_packet_data.scarecrow_application.unique_id = 'AcmeCorp1572566399123'
body.document_packet_data.scarecrow_application.country = 'USA'
body.document_packet_data.scarecrow_application.principal = Person()
body.document_packet_data.scarecrow_application.principal.name = Name()
body.document_packet_data.scarecrow_application.principal.name.first_name = 'John'
body.document_packet_data.scarecrow_application.principal.name.last_name = 'Doe'
body.document_packet_data.scarecrow_application.principal.positions = {'key0' : False, 'key1' : True, 'key2' : False } 
body.document_packet_data.scarecrow_application.business_info = BusinessInfo()
body.document_packet_data.scarecrow_application.business_info.dba_name = 'Grimm\'s Bookstore'
body.document_packet_data.scarecrow_application.business_info.dba_name_extended = 'Grimm\'s Fairytales and Other Stories Bookstore'
body.document_packet_data.scarecrow_application.business_info.business_address = Address()
body.document_packet_data.scarecrow_application.business_info.business_address.street_name = 'Baker Street'
body.document_packet_data.scarecrow_application.business_info.business_address.city = 'Atlanta'
body.document_packet_data.scarecrow_application.business_info.business_address.country = 'USA'
body.document_packet_data.scarecrow_application.business_info.legal_name = 'Barkers Dog Bakery'
body.document_packet_data.scarecrow_application.business_info.legal_name_extended = 'Baking Better Biscuits for Your Favorite Barkers Dog Bakery LLC'
body.document_packet_data.scarecrow_application.business_info.additional_addresses = Address()
body.document_packet_data.scarecrow_application.business_info.additional_addresses.street_name = None
body.document_packet_data.scarecrow_application.business_info.additional_addresses.city = None
body.document_packet_data.scarecrow_application.business_info.additional_addresses.country = None
body.document_packet_data.scarecrow_application.business_info.ownership_type = OwnershipTypeEnum.LIMITED_PARTNERSHIP
body.document_packet_data.scarecrow_application.business_info.product_description = 'Bakeries'
body.document_packet_data.scarecrow_application.business_info.mcc_code = '7399E'
body.document_packet_data.scarecrow_application.business_info.establishment_year = '2005'
body.document_packet_data.scarecrow_application.business_info.current_ownership_years = '3'
body.document_packet_data.scarecrow_application.business_info.current_ownership_months = '6'
body.document_packet_data.scarecrow_application.business_info.communication_language = 'en'
body.document_packet_data.scarecrow_application.business_info.pos_language = 'en'
body.document_packet_data.scarecrow_application.financial_info = FinancialInfo()
body.document_packet_data.scarecrow_application.financial_info.avg_sale_amount = '125'
body.document_packet_data.scarecrow_application.financial_info.monthly_card_sales = '1000'
body.document_packet_data.scarecrow_application.financial_info.card_present_acceptance_percent = '100'
body.document_packet_data.scarecrow_application.financial_info.internet_acceptance_percent = '0'
body.document_packet_data.scarecrow_application.financial_info.moto_acceptance_percent = '0'
body.document_packet_data.scarecrow_application.sales_rep_code = '12345'
body.document_packet_data.scarecrow_application.contact = Person()
body.document_packet_data.scarecrow_application.contact.name = Name()
body.document_packet_data.scarecrow_application.contact.name.first_name = 'John'
body.document_packet_data.scarecrow_application.contact.name.last_name = 'Doe'
body.document_packet_data.scarecrow_application.contact.positions = {'key0' : False, 'key1' : True } 
body.document_packet_data.scarecrow_application.bank_accounts = BankingInfo()
body.document_packet_data.scarecrow_application.bank_accounts.funding_method = envrr
body.document_packet_data.scarecrow_application.bank_accounts.account_number = None
body.document_packet_data.scarecrow_application.bank_accounts.sort_code = None
body.document_packet_data.scarecrow_application.card_pricing = CardPricing()
body.document_packet_data.scarecrow_application.card_pricing.pricing_method = PricingMethodEnum.TIERED_PRICING
body.document_packet_data.scarecrow_application.card_pricing.pricing_category = PricingCategoryEnum.INTERNET
body.document_packet_data.scarecrow_application.card_pricing.card_charges = []

body.document_packet_data.scarecrow_application.card_pricing.card_charges.append(CardCharge())
body.document_packet_data.scarecrow_application.card_pricing.card_charges[0].card_type = CardTypeEnum.UK_DOMESTIC_MAESTRO

body.document_packet_data.scarecrow_application.parent_entity = 'parentEntity4'
body.document_packet_data.language = 'language2'
body.document_packet_data.vendor_info = ProviderInfo()
body.document_packet_data.bank_account_details_map = BankAccountAdditionalInfo()
body.document_packet_data.displayed_currency = 'displayedCurrency8'

result = satid_api_controller.append_group_document_packet(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Create Document Packet

Create a document packet

```python
def create_document_packet(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateDocumentPacketRequest`](../../doc/models/create-document-packet-request.md) | Body, Required | - |

## Response Type

[`CreateDocumentPacketResponse`](../../doc/models/create-document-packet-response.md)

## Example Usage

```python
body = CreateDocumentPacketRequest()
body.profile_code = 'TEST'
body.signers = []

body.signers.append(Signer())
body.signers[0].signer_id = 'signerId4'
body.signers[0].signer = Name()
body.signers[0].signer.first_name = 'John'
body.signers[0].signer.last_name = 'Doe'
body.signers[0].principal = False

body.signers.append(Signer())
body.signers[1].signer_id = 'signerId5'
body.signers[1].signer = Name()
body.signers[1].signer.first_name = 'John'
body.signers[1].signer.last_name = 'Doe'
body.signers[1].principal = True

body.signers.append(Signer())
body.signers[2].signer_id = 'signerId6'
body.signers[2].signer = Name()
body.signers[2].signer.first_name = 'John'
body.signers[2].signer.last_name = 'Doe'
body.signers[2].principal = False

body.document_packet_data = DocumentPacketData()
body.document_packet_data.scarecrow_application = ScarecrowApplication()
body.document_packet_data.scarecrow_application.client_id = 'IDNA'
body.document_packet_data.scarecrow_application.unique_id = 'AcmeCorp1572566399123'
body.document_packet_data.scarecrow_application.country = 'USA'
body.document_packet_data.scarecrow_application.principal = Person()
body.document_packet_data.scarecrow_application.principal.name = Name()
body.document_packet_data.scarecrow_application.principal.name.first_name = 'John'
body.document_packet_data.scarecrow_application.principal.name.last_name = 'Doe'
body.document_packet_data.scarecrow_application.principal.positions = {'key0' : False, 'key1' : True, 'key2' : False } 
body.document_packet_data.scarecrow_application.business_info = BusinessInfo()
body.document_packet_data.scarecrow_application.business_info.dba_name = 'Grimm\'s Bookstore'
body.document_packet_data.scarecrow_application.business_info.dba_name_extended = 'Grimm\'s Fairytales and Other Stories Bookstore'
body.document_packet_data.scarecrow_application.business_info.business_address = Address()
body.document_packet_data.scarecrow_application.business_info.business_address.street_name = 'Baker Street'
body.document_packet_data.scarecrow_application.business_info.business_address.city = 'Atlanta'
body.document_packet_data.scarecrow_application.business_info.business_address.country = 'USA'
body.document_packet_data.scarecrow_application.business_info.legal_name = 'Barkers Dog Bakery'
body.document_packet_data.scarecrow_application.business_info.legal_name_extended = 'Baking Better Biscuits for Your Favorite Barkers Dog Bakery LLC'
body.document_packet_data.scarecrow_application.business_info.additional_addresses = Address()
body.document_packet_data.scarecrow_application.business_info.additional_addresses.street_name = None
body.document_packet_data.scarecrow_application.business_info.additional_addresses.city = None
body.document_packet_data.scarecrow_application.business_info.additional_addresses.country = None
body.document_packet_data.scarecrow_application.business_info.ownership_type = OwnershipTypeEnum.LIMITED_PARTNERSHIP
body.document_packet_data.scarecrow_application.business_info.product_description = 'Bakeries'
body.document_packet_data.scarecrow_application.business_info.mcc_code = '7399E'
body.document_packet_data.scarecrow_application.business_info.establishment_year = '2005'
body.document_packet_data.scarecrow_application.business_info.current_ownership_years = '3'
body.document_packet_data.scarecrow_application.business_info.current_ownership_months = '6'
body.document_packet_data.scarecrow_application.business_info.communication_language = 'en'
body.document_packet_data.scarecrow_application.business_info.pos_language = 'en'
body.document_packet_data.scarecrow_application.financial_info = FinancialInfo()
body.document_packet_data.scarecrow_application.financial_info.avg_sale_amount = '125'
body.document_packet_data.scarecrow_application.financial_info.monthly_card_sales = '1000'
body.document_packet_data.scarecrow_application.financial_info.card_present_acceptance_percent = '100'
body.document_packet_data.scarecrow_application.financial_info.internet_acceptance_percent = '0'
body.document_packet_data.scarecrow_application.financial_info.moto_acceptance_percent = '0'
body.document_packet_data.scarecrow_application.sales_rep_code = '12345'
body.document_packet_data.scarecrow_application.contact = Person()
body.document_packet_data.scarecrow_application.contact.name = Name()
body.document_packet_data.scarecrow_application.contact.name.first_name = 'John'
body.document_packet_data.scarecrow_application.contact.name.last_name = 'Doe'
body.document_packet_data.scarecrow_application.contact.positions = {'key0' : False, 'key1' : True } 
body.document_packet_data.scarecrow_application.bank_accounts = BankingInfo()
body.document_packet_data.scarecrow_application.bank_accounts.funding_method = envrr
body.document_packet_data.scarecrow_application.bank_accounts.account_number = None
body.document_packet_data.scarecrow_application.bank_accounts.sort_code = None
body.document_packet_data.scarecrow_application.card_pricing = CardPricing()
body.document_packet_data.scarecrow_application.card_pricing.pricing_method = PricingMethodEnum.TIERED_PRICING
body.document_packet_data.scarecrow_application.card_pricing.pricing_category = PricingCategoryEnum.INTERNET
body.document_packet_data.scarecrow_application.card_pricing.card_charges = []

body.document_packet_data.scarecrow_application.card_pricing.card_charges.append(CardCharge())
body.document_packet_data.scarecrow_application.card_pricing.card_charges[0].card_type = CardTypeEnum.UK_DOMESTIC_MAESTRO

body.document_packet_data.scarecrow_application.parent_entity = 'parentEntity4'
body.document_packet_data.language = 'language2'
body.document_packet_data.vendor_info = ProviderInfo()
body.document_packet_data.bank_account_details_map = BankAccountAdditionalInfo()
body.document_packet_data.displayed_currency = 'displayedCurrency8'

result = satid_api_controller.create_document_packet(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Credit Check

Credit Check

```python
def credit_check(self,
                version_number,
                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version_number` | `int` | Template, Required | **Constraints**: *Pattern*: `[1-4]` |
| `body` | [`ScarecrowApplication`](../../doc/models/scarecrow-application.md) | Body, Required | - |

## Response Type

[`CreditCheckResponse`](../../doc/models/credit-check-response.md)

## Example Usage

```python
version_number = 66
body = ScarecrowApplication()
body.client_id = 'IDNA'
body.unique_id = 'AcmeCorp1572566399123'
body.country = 'USA'
body.principal = Person()
body.principal.name = Name()
body.principal.name.first_name = 'John'
body.principal.name.last_name = 'Doe'
body.principal.positions = {'key0' : False } 
body.business_info = BusinessInfo()
body.business_info.dba_name = 'Grimm\'s Bookstore'
body.business_info.dba_name_extended = 'Grimm\'s Fairytales and Other Stories Bookstore'
body.business_info.business_address = Address()
body.business_info.business_address.street_name = 'Baker Street'
body.business_info.business_address.city = 'Atlanta'
body.business_info.business_address.country = 'USA'
body.business_info.legal_name = 'Barkers Dog Bakery'
body.business_info.legal_name_extended = 'Baking Better Biscuits for Your Favorite Barkers Dog Bakery LLC'
body.business_info.additional_addresses = Address()
body.business_info.additional_addresses.street_name = None
body.business_info.additional_addresses.city = None
body.business_info.additional_addresses.country = None
body.business_info.ownership_type = OwnershipTypeEnum.PARTNERSHIP_LIMITED_BY_SHARES
body.business_info.product_description = 'Bakeries'
body.business_info.mcc_code = '7399E'
body.business_info.establishment_year = '2005'
body.business_info.current_ownership_years = '3'
body.business_info.current_ownership_months = '6'
body.business_info.communication_language = 'en'
body.business_info.pos_language = 'en'
body.financial_info = FinancialInfo()
body.financial_info.avg_sale_amount = '125'
body.financial_info.monthly_card_sales = '1000'
body.financial_info.card_present_acceptance_percent = '100'
body.financial_info.internet_acceptance_percent = '0'
body.financial_info.moto_acceptance_percent = '0'
body.sales_rep_code = '12345'
body.contact = Person()
body.contact.name = Name()
body.contact.name.first_name = 'John'
body.contact.name.last_name = 'Doe'
body.contact.positions = {'key0' : False } 
body.bank_accounts = BankingInfo()
body.bank_accounts.funding_method = envrr
body.bank_accounts.account_number = None
body.bank_accounts.sort_code = None
body.card_pricing = CardPricing()
body.card_pricing.pricing_method = PricingMethodEnum.CLEAR_AND_SIMPLE
body.card_pricing.pricing_category = PricingCategoryEnum.RETAIL
body.card_pricing.card_charges = []

body.card_pricing.card_charges.append(CardCharge())
body.card_pricing.card_charges[0].card_type = CardTypeEnum.VISA_DEBIT

body.card_pricing.card_charges.append(CardCharge())
body.card_pricing.card_charges[1].card_type = CardTypeEnum.VPAY

body.parent_entity = 'parentEntity8'

result = satid_api_controller.credit_check(version_number, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Update Document Packet Data

Update document packet

```python
def update_document_packet_data(self,
                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UpdateDocumentPacketDataRequest`](../../doc/models/update-document-packet-data-request.md) | Body, Required | - |

## Response Type

[`UpdateDocumentPacketDataResponse`](../../doc/models/update-document-packet-data-response.md)

## Example Usage

```python
body = UpdateDocumentPacketDataRequest()
body.document_packet_id = 'documentPacketId2'
body.document_packet_data = DocumentPacketData()
body.document_packet_data.scarecrow_application = ScarecrowApplication()
body.document_packet_data.scarecrow_application.client_id = 'IDNA'
body.document_packet_data.scarecrow_application.unique_id = 'AcmeCorp1572566399123'
body.document_packet_data.scarecrow_application.country = 'USA'
body.document_packet_data.scarecrow_application.principal = Person()
body.document_packet_data.scarecrow_application.principal.name = Name()
body.document_packet_data.scarecrow_application.principal.name.first_name = 'John'
body.document_packet_data.scarecrow_application.principal.name.last_name = 'Doe'
body.document_packet_data.scarecrow_application.principal.positions = {'key0' : False, 'key1' : True, 'key2' : False } 
body.document_packet_data.scarecrow_application.business_info = BusinessInfo()
body.document_packet_data.scarecrow_application.business_info.dba_name = 'Grimm\'s Bookstore'
body.document_packet_data.scarecrow_application.business_info.dba_name_extended = 'Grimm\'s Fairytales and Other Stories Bookstore'
body.document_packet_data.scarecrow_application.business_info.business_address = Address()
body.document_packet_data.scarecrow_application.business_info.business_address.street_name = 'Baker Street'
body.document_packet_data.scarecrow_application.business_info.business_address.city = 'Atlanta'
body.document_packet_data.scarecrow_application.business_info.business_address.country = 'USA'
body.document_packet_data.scarecrow_application.business_info.legal_name = 'Barkers Dog Bakery'
body.document_packet_data.scarecrow_application.business_info.legal_name_extended = 'Baking Better Biscuits for Your Favorite Barkers Dog Bakery LLC'
body.document_packet_data.scarecrow_application.business_info.additional_addresses = Address()
body.document_packet_data.scarecrow_application.business_info.additional_addresses.street_name = None
body.document_packet_data.scarecrow_application.business_info.additional_addresses.city = None
body.document_packet_data.scarecrow_application.business_info.additional_addresses.country = None
body.document_packet_data.scarecrow_application.business_info.ownership_type = OwnershipTypeEnum.LIMITED_PARTNERSHIP
body.document_packet_data.scarecrow_application.business_info.product_description = 'Bakeries'
body.document_packet_data.scarecrow_application.business_info.mcc_code = '7399E'
body.document_packet_data.scarecrow_application.business_info.establishment_year = '2005'
body.document_packet_data.scarecrow_application.business_info.current_ownership_years = '3'
body.document_packet_data.scarecrow_application.business_info.current_ownership_months = '6'
body.document_packet_data.scarecrow_application.business_info.communication_language = 'en'
body.document_packet_data.scarecrow_application.business_info.pos_language = 'en'
body.document_packet_data.scarecrow_application.financial_info = FinancialInfo()
body.document_packet_data.scarecrow_application.financial_info.avg_sale_amount = '125'
body.document_packet_data.scarecrow_application.financial_info.monthly_card_sales = '1000'
body.document_packet_data.scarecrow_application.financial_info.card_present_acceptance_percent = '100'
body.document_packet_data.scarecrow_application.financial_info.internet_acceptance_percent = '0'
body.document_packet_data.scarecrow_application.financial_info.moto_acceptance_percent = '0'
body.document_packet_data.scarecrow_application.sales_rep_code = '12345'
body.document_packet_data.scarecrow_application.contact = Person()
body.document_packet_data.scarecrow_application.contact.name = Name()
body.document_packet_data.scarecrow_application.contact.name.first_name = 'John'
body.document_packet_data.scarecrow_application.contact.name.last_name = 'Doe'
body.document_packet_data.scarecrow_application.contact.positions = {'key0' : False, 'key1' : True } 
body.document_packet_data.scarecrow_application.bank_accounts = BankingInfo()
body.document_packet_data.scarecrow_application.bank_accounts.funding_method = envrr
body.document_packet_data.scarecrow_application.bank_accounts.account_number = None
body.document_packet_data.scarecrow_application.bank_accounts.sort_code = None
body.document_packet_data.scarecrow_application.card_pricing = CardPricing()
body.document_packet_data.scarecrow_application.card_pricing.pricing_method = PricingMethodEnum.TIERED_PRICING
body.document_packet_data.scarecrow_application.card_pricing.pricing_category = PricingCategoryEnum.INTERNET
body.document_packet_data.scarecrow_application.card_pricing.card_charges = []

body.document_packet_data.scarecrow_application.card_pricing.card_charges.append(CardCharge())
body.document_packet_data.scarecrow_application.card_pricing.card_charges[0].card_type = CardTypeEnum.UK_DOMESTIC_MAESTRO

body.document_packet_data.scarecrow_application.parent_entity = 'parentEntity4'
body.document_packet_data.language = 'language2'
body.document_packet_data.vendor_info = ProviderInfo()
body.document_packet_data.bank_account_details_map = BankAccountAdditionalInfo()
body.document_packet_data.displayed_currency = 'displayedCurrency8'

result = satid_api_controller.update_document_packet_data(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Check Document Signing Status

Check the signing status of one or more signer of a packet

```python
def check_document_signing_status(self,
                                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CheckDocumentSigningStatusRequest`](../../doc/models/check-document-signing-status-request.md) | Body, Required | - |

## Response Type

[`CheckDocumentSigningStatusResponse`](../../doc/models/check-document-signing-status-response.md)

## Example Usage

```python
body = CheckDocumentSigningStatusRequest()

result = satid_api_controller.check_document_signing_status(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Delete Document Packet

Delete a Document Packet

```python
def delete_document_packet(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeleteDocumentPacketRequest`](../../doc/models/delete-document-packet-request.md) | Body, Required | - |

## Response Type

[`DeleteDocumentPacketResponse`](../../doc/models/delete-document-packet-response.md)

## Example Usage

```python
body = DeleteDocumentPacketRequest()

result = satid_api_controller.delete_document_packet(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Delete Group Document Packet

Delete Group Document Packet

```python
def delete_group_document_packet(self,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeleteGroupDocumentPacketRequest`](../../doc/models/delete-group-document-packet-request.md) | Body, Required | - |

## Response Type

[`DeleteGroupDocumentPacketResponse`](../../doc/models/delete-group-document-packet-response.md)

## Example Usage

```python
body = DeleteGroupDocumentPacketRequest()

result = satid_api_controller.delete_group_document_packet(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Update Document Packet

Update Document Packet

```python
def update_document_packet(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UpdateDocumentPacketRequest`](../../doc/models/update-document-packet-request.md) | Body, Required | - |

## Response Type

[`UpdateDocumentPacketResponse`](../../doc/models/update-document-packet-response.md)

## Example Usage

```python
body = UpdateDocumentPacketRequest()
body.document_packet_id = 'documentPacketId2'

result = satid_api_controller.update_document_packet(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Execute Group Document Packet

Execute Document Packet

```python
def execute_group_document_packet(self,
                                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ExecuteGroupDocumentPacketRequest`](../../doc/models/execute-group-document-packet-request.md) | Body, Required | - |

## Response Type

[`ExecuteGroupDocumentPacketResponse`](../../doc/models/execute-group-document-packet-response.md)

## Example Usage

```python
body = ExecuteGroupDocumentPacketRequest()
body.group_document_packet_id = 'groupDocumentPacketId4'

result = satid_api_controller.execute_group_document_packet(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Get Unsigned Document Content

Get unsigned document packet singular document

```python
def get_unsigned_document_content(self,
                                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetUnsignedDocumentRequest`](../../doc/models/get-unsigned-document-request.md) | Body, Required | - |

## Response Type

[`GetDocumentResponse`](../../doc/models/get-document-response.md)

## Example Usage

```python
body = GetUnsignedDocumentRequest()

result = satid_api_controller.get_unsigned_document_content(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |


# Get Unsigned Documents Packet Content

Get unsigned document packet full content

```python
def get_unsigned_documents_packet_content(self,
                                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetUnsignedDocumentsPacketRequest`](../../doc/models/get-unsigned-documents-packet-request.md) | Body, Required | - |

## Response Type

[`GetDocumentsResponse`](../../doc/models/get-documents-response.md)

## Example Usage

```python
body = GetUnsignedDocumentsPacketRequest()

result = satid_api_controller.get_unsigned_documents_packet_content(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |

