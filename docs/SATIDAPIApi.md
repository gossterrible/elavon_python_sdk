# elavon.SATIDAPIApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**answer_quiz**](SATIDAPIApi.md#answer_quiz) | **POST** /v{versionNumber}/answerquiz | Answer KYC Quiz
[**answer_quiz_xsd_schema**](SATIDAPIApi.md#answer_quiz_xsd_schema) | **GET** /v{versionNumber}/answerquiz/schema.xsd | Get Quiz Answer Schema
[**append_group_document_packet**](SATIDAPIApi.md#append_group_document_packet) | **POST** /appendgroupdocumentpacket | Append to Group Document Packet
[**bank_validate**](SATIDAPIApi.md#bank_validate) | **POST** /v{versionNumber}/bank | Validate Bank Account
[**bank_xsd_schema**](SATIDAPIApi.md#bank_xsd_schema) | **GET** /v{versionNumber}/bank/schema.xsd | Get Bank Account Validation Schema
[**board**](SATIDAPIApi.md#board) | **POST** /v{versionNumber}/board | Boarding
[**board_status**](SATIDAPIApi.md#board_status) | **POST** /v{versionNumber}/boardstatus | Boarding Status
[**board_status_xsd_schema**](SATIDAPIApi.md#board_status_xsd_schema) | **GET** /v{versionNumber}/boardstatus/schema.xsd | Get Boarding Status Schema
[**board_xsd_schema**](SATIDAPIApi.md#board_xsd_schema) | **GET** /v{versionNumber}/{iso3Country}/board/schema.xsd | Get Boarding Schema
[**check_document_signing_status**](SATIDAPIApi.md#check_document_signing_status) | **POST** /checkdocumentsignerstatus | Check the signing status of one or more signer of a packet
[**create_document_packet**](SATIDAPIApi.md#create_document_packet) | **POST** /createdocumentpacket | Create a document packet
[**create_group_document_packet**](SATIDAPIApi.md#create_group_document_packet) | **POST** /creategroupdocumentpacket | Create Group Document Packet
[**credit_check**](SATIDAPIApi.md#credit_check) | **POST** /v{versionNumber}/creditcheck | Credit Check
[**credit_check_xsd_schema**](SATIDAPIApi.md#credit_check_xsd_schema) | **GET** /v{versionNumber}/{iso3Country}/creditcheck/schema.xsd | Get Credit Check Schema
[**delete_document_packet**](SATIDAPIApi.md#delete_document_packet) | **POST** /deletedocumentpacket | Delete a Document Packet
[**delete_group_document_packet**](SATIDAPIApi.md#delete_group_document_packet) | **POST** /deletegroupdocumentpacket | Delete Group Document Packet
[**execute_group_document_packet**](SATIDAPIApi.md#execute_group_document_packet) | **POST** /executegroupdocumentpacket | Execute Document Packet
[**generate_packet_documents**](SATIDAPIApi.md#generate_packet_documents) | **POST** /generatepacketdocuments | Trigger generation of document in packet for submission
[**get_presented_documents**](SATIDAPIApi.md#get_presented_documents) | **POST** /getdocuments | Get all documents to present to the user
[**get_quiz**](SATIDAPIApi.md#get_quiz) | **POST** /v{versionNumber}/getquiz | Request KYC Quiz
[**get_quiz_xsd_schema**](SATIDAPIApi.md#get_quiz_xsd_schema) | **GET** /v{versionNumber}/getquiz/schema.xsd | Get Quiz Request Schema
[**get_signed_document_packet_content**](SATIDAPIApi.md#get_signed_document_packet_content) | **POST** /getsignedpacket | Get signed document packet content
[**get_terminal_ids**](SATIDAPIApi.md#get_terminal_ids) | **POST** /getterminalids | Get terminal ids and related information for MID
[**get_unsigned_document_content**](SATIDAPIApi.md#get_unsigned_document_content) | **POST** /getunsigneddocument | Get unsigned document packet singular document
[**get_unsigned_documents_packet_content**](SATIDAPIApi.md#get_unsigned_documents_packet_content) | **POST** /getunsignedpacket | Get unsigned document packet full content
[**list_packet_presented_documents**](SATIDAPIApi.md#list_packet_presented_documents) | **POST** /listpacketdocuments | List Packet Documents to present to the user
[**list_presented_documents**](SATIDAPIApi.md#list_presented_documents) | **POST** /listdocuments | List Documents to present to the user
[**post_code_xsd_schema**](SATIDAPIApi.md#post_code_xsd_schema) | **GET** /v{versionNumber}/postal/schema.xsd | Get Postal Code Validation Schema
[**postal_validate**](SATIDAPIApi.md#postal_validate) | **POST** /v{versionNumber}/postal | Validate Postal Code
[**refresh_signer_user_sessions**](SATIDAPIApi.md#refresh_signer_user_sessions) | **POST** /refreshsignerusersessions | Refresh the session for signers of a document packet
[**regenerate_packet_documents**](SATIDAPIApi.md#regenerate_packet_documents) | **POST** /regeneratesignedpacket | Regenerate signed Packet Content in event of failure
[**update_document_packet**](SATIDAPIApi.md#update_document_packet) | **POST** /updatedocumentpacket | Update Document Packet
[**update_document_packet_data**](SATIDAPIApi.md#update_document_packet_data) | **POST** /updatedocumentpacketdata | Update document packet
[**upload_document_xsd_schema**](SATIDAPIApi.md#upload_document_xsd_schema) | **GET** /v{versionNumber}/uploadDocuments/schema.xsd | Get Upload Documents Schema
[**upload_documents**](SATIDAPIApi.md#upload_documents) | **POST** /v{versionNumber}/uploadDocuments | Upload Documents


# **answer_quiz**
> AnswerQuizResponse answer_quiz(version_number, body)

Answer KYC Quiz

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.answer_quiz_request import AnswerQuizRequest
from elavon.model.answer_quiz_response import AnswerQuizResponse
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    version_number = 1 # int | 
    body = AnswerQuizRequest(
        id="id_example",
        mid="mid_example",
        email="email_example",
        legal_name="legal_name_example",
        vat_id="vat_id_example",
        cc_email="cc_email_example",
        opt_out=True,
        marketing_data_consent_map={
            "key": True,
        },
        quiz_id=1,
        transaction_key="transaction_key_example",
        quiz_answers=[
            QuizAnswer(
                question_number=1,
                answer_number=1,
            ),
        ],
        country="country_example",
    ) # AnswerQuizRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Answer KYC Quiz
        api_response = api_instance.answer_quiz(version_number, body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->answer_quiz: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_number** | **int**|  |
 **body** | [**AnswerQuizRequest**](AnswerQuizRequest.md)|  |

### Return type

[**AnswerQuizResponse**](AnswerQuizResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Answer Quiz Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **answer_quiz_xsd_schema**
> answer_quiz_xsd_schema(version_number)

Get Quiz Answer Schema

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    version_number = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get Quiz Answer Schema
        api_instance.answer_quiz_xsd_schema(version_number)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->answer_quiz_xsd_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_number** | **int**|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_group_document_packet**
> AppendGroupDocumentPacketResponse append_group_document_packet(body)

Append to Group Document Packet

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.append_group_document_packet_request import AppendGroupDocumentPacketRequest
from elavon.model.append_group_document_packet_response import AppendGroupDocumentPacketResponse
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = AppendGroupDocumentPacketRequest(
        group_document_packet_id="group_document_packet_id_example",
        profile_code="profile_code_example",
        signers=[
            Signer(
                signer_id="signer_id_example",
                signer=Name(
                    salutation="MR",
                    first_name="John",
                    middle_name="Lee",
                    last_name="Doe",
                ),
                email_address="email_address_example",
                principal=True,
                signing_complete_url="signing_complete_url_example",
                signing_decline_url="signing_decline_url_example",
                signing_expired_url="signing_expired_url_example",
                language="language_example",
                opt_in_out1=True,
                opt_in_out2=True,
                opt_in_out3=True,
            ),
        ],
        document_packet_data=DocumentPacketData(
            scarecrow_application=ScarecrowApplication(
                client_id="IDNA",
                client_group_number="860",
                unique_id="AcmeCorp1572566399123",
                banker_id="123",
                banker_partner_id="123",
                country="USA",
                principal=Person(
                    name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    contact_info=ContactInfo(
                        address=Address(
                            street_name="Baker Street",
                            street_number="221",
                            line_two="Apt B",
                            line_three="48",
                            city="Atlanta",
                            county="Fulton",
                            post_code="30346",
                            country="USA",
                            state="USA_AL",
                            classification="BUSINESS_STREET_ADDRESS",
                            contact_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            location_name="Baker Plaza",
                        ),
                        additional_addresses={
                            "key": Address(
                                street_name="Baker Street",
                                street_number="221",
                                line_two="Apt B",
                                line_three="48",
                                city="Atlanta",
                                county="Fulton",
                                post_code="30346",
                                country="USA",
                                state="USA_AL",
                                classification="BUSINESS_STREET_ADDRESS",
                                contact_name=Name(
                                    salutation="MR",
                                    first_name="John",
                                    middle_name="Lee",
                                    last_name="Doe",
                                ),
                                location_name="Baker Plaza",
                            ),
                        },
                        phone=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        mobile=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        fax=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        email_address="contactname@email.com",
                    ),
                    dob=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    positions={
                        "key": True,
                    },
                    ownership_pct="90",
                    ids=[
                        Identification(
                            id_type="PASSPORT",
                            id_number="123456789",
                            expiry_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issue_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issuing_country="USA",
                            issuing_state="USA_AL",
                            id_name="id_name_example",
                            issuing_agency="issuing_agency_example",
                        ),
                    ],
                    title_type="ACCOUNTING_MANAGER",
                    title="Chief Technology Officer",
                    signing_personal_guarantee=True,
                    responsible_party=True,
                    related_party=True,
                    residing_country="GBR",
                    primary_nationality="GBR",
                    secondary_nationality="IRL",
                    documentary_info=DocumentaryInfo(
                        documentary=True,
                        documentary_verifier="SALES_TEAM",
                        documentary_issuer="USA",
                        documentary_type="DRIVER_LICENSE",
                        id_number="111111117",
                        issue_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        expiry_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        issuing_state="USA_AL",
                        foreign_issuing_state="foreign_issuing_state_example",
                    ),
                    alternate_address_info=AlternateAddressInfo(
                        document_needed=True,
                        document_verified=True,
                        alternate_address_document_type="BANK_STATEMENT",
                        document_name="document_name_example",
                    ),
                    is_new_owner=True,
                    directional_ownership_type="DIRECT_OWNERSHIP",
                    signing_agreement=True,
                    us_person=True,
                ),
                business_info=BusinessInfo(
                    dba_name="Grimm's Bookstore",
                    dba_name_extended="Grimm's Fairytales and Other Stories Bookstore",
                    business_address=Address(
                        street_name="Baker Street",
                        street_number="221",
                        line_two="Apt B",
                        line_three="48",
                        city="Atlanta",
                        county="Fulton",
                        post_code="30346",
                        country="USA",
                        state="USA_AL",
                        classification="BUSINESS_STREET_ADDRESS",
                        contact_name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        location_name="Baker Plaza",
                    ),
                    legal_name="Barkers Dog Bakery",
                    legal_name_extended="Baking Better Biscuits for Your Favorite Barkers Dog Bakery LLC",
                    legal_name_marked=[
                        "legal_name_marked_example",
                    ],
                    additional_addresses={
                        "key": Address(
                            street_name="Baker Street",
                            street_number="221",
                            line_two="Apt B",
                            line_three="48",
                            city="Atlanta",
                            county="Fulton",
                            post_code="30346",
                            country="USA",
                            state="USA_AL",
                            classification="BUSINESS_STREET_ADDRESS",
                            contact_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            location_name="Baker Plaza",
                        ),
                    },
                    ownership_type="SOLE_TRADER",
                    registration_number="1234567",
                    tax_id="787421357",
                    tax_id_type="FEDERAL_TAX_ID",
                    vat_info=VatInfo(
                        number_option="VAT_NBR",
                        number56_b="123456789",
                        expiry_date56_b=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        tax_number_type="CORPORATE_TAX_NUMBER",
                        tax_number="tax_number_example",
                    ),
                    tax_form_type="W9",
                    tax_class_type="CORPORATION",
                    customer_membership_number="111222",
                    product_description="Bakeries",
                    mcc_code="7399E",
                    establishment_year="2005",
                    current_ownership_years="3",
                    current_ownership_months="6",
                    government_owned_entity=True,
                    communication_language="en",
                    pos_language="en",
                    store_number="123456789",
                    association_codes=[
                        "12345",
                    ],
                    opt_out=True,
                    sign_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    pci_info=PCIInfo(
                        pci_program_level="ONE",
                        pci_service_type="BASIC",
                        pci_contact_first_name="pci_contact_first_name_example",
                        pci_contact_last_name="pci_contact_last_name_example",
                        pci_contact_email_address="pci_contact_email_address_example",
                        pci_contact_phone=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        pci_groups=[
                            "PCI_PROGRAM_EXCLUSION",
                        ],
                    ),
                    employer_id="1234567",
                    country_of_origin="USA",
                    exemption_type="ADDITIONAL_LOCATION",
                    owner_exemption_type="BANK_ADVISED_POOLED",
                    number_of_partners="ONE",
                    relationship_mgr_code="1234567",
                    country_of_primary_operation="USA",
                    bearer_shares=True,
                    legal_status="CERTIFIED_INCORPORATION_ARTICLES",
                    verifications={
                        "key": VerificationInfo(
                            documentary=True,
                            issuing_country="USA",
                            issuing_state="USA_AL",
                            site_person_met="John Smith",
                            site_visit_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            id_number="111111117",
                            issue_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            expiry_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            document_type="CERTIFIED_INCORPORATION_ARTICLES",
                        ),
                    },
                    industry_class="LODGING",
                    no_plates=True,
                    agent_number="1223334",
                    location_mid_range="NORDIC",
                    hemp_grower_info=HempGrowerInfo(
                        operations_description="operations_description_example",
                        is_licensed=True,
                        license_expiration_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        additional_mrb_activity=True,
                        cannabis_revenue_percentage_range="NONE",
                    ),
                    credit_decision_info=CreditDecisionInfo(
                        credit_decision_flag=True,
                        credit_decision_id="credit_decision_id_example",
                    ),
                ),
                financial_info=FinancialInfo(
                    avg_sale_amount="125",
                    monthly_card_sales="1000",
                    annual_card_sales="12000",
                    annual_revenue="240000",
                    highest_ticket_amount="1000",
                    highest_ticket_frequency=1,
                    funding_currency="USD",
                    card_present_acceptance_percent="100",
                    internet_acceptance_percent="0",
                    moto_acceptance_percent="0",
                    business_email_address="business_email_address_example",
                    business_website_url="business@email.com",
                    customer_service_phone=PhoneNumber(
                        intl_code="44",
                        area_code="111",
                        number="1231234",
                        extension="2",
                    ),
                    not_present_delay_days=0,
                    deposit_frequency="0",
                    deposit_size_percent="1",
                    deposit_balance_days="1",
                    deposit_fulfillment_days="1",
                    full_payment_percent="1",
                    full_payment_fulfillment="1",
                    utilize_cvv2=True,
                    recurring_transactions=True,
                    contract_term_type="ZERO_MONTH",
                    months_closed=[
                        "JAN",
                    ],
                    monetary_billing_method="CARD_DISCOUNT",
                    authorization_included=True,
                    annual_fee_month_start="JAN",
                    money_services=True,
                    payment_services=True,
                    third_party_processor=True,
                    non_government_non_profit=True,
                    daily_discount=True,
                    non_bank_atm=True,
                    embassy=True,
                    high_inter_annual_trans_ngo=True,
                ),
                sales_rep_code="12345",
                additional_shareholders=[
                    Person(
                        name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        contact_info=ContactInfo(
                            address=Address(
                                street_name="Baker Street",
                                street_number="221",
                                line_two="Apt B",
                                line_three="48",
                                city="Atlanta",
                                county="Fulton",
                                post_code="30346",
                                country="USA",
                                state="USA_AL",
                                classification="BUSINESS_STREET_ADDRESS",
                                contact_name=Name(
                                    salutation="MR",
                                    first_name="John",
                                    middle_name="Lee",
                                    last_name="Doe",
                                ),
                                location_name="Baker Plaza",
                            ),
                            additional_addresses={
                                "key": Address(
                                    street_name="Baker Street",
                                    street_number="221",
                                    line_two="Apt B",
                                    line_three="48",
                                    city="Atlanta",
                                    county="Fulton",
                                    post_code="30346",
                                    country="USA",
                                    state="USA_AL",
                                    classification="BUSINESS_STREET_ADDRESS",
                                    contact_name=Name(
                                        salutation="MR",
                                        first_name="John",
                                        middle_name="Lee",
                                        last_name="Doe",
                                    ),
                                    location_name="Baker Plaza",
                                ),
                            },
                            phone=PhoneNumber(
                                intl_code="44",
                                area_code="111",
                                number="1231234",
                                extension="2",
                            ),
                            mobile=PhoneNumber(
                                intl_code="44",
                                area_code="111",
                                number="1231234",
                                extension="2",
                            ),
                            fax=PhoneNumber(
                                intl_code="44",
                                area_code="111",
                                number="1231234",
                                extension="2",
                            ),
                            email_address="contactname@email.com",
                        ),
                        dob=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        positions={
                            "key": True,
                        },
                        ownership_pct="90",
                        ids=[
                            Identification(
                                id_type="PASSPORT",
                                id_number="123456789",
                                expiry_date=DateComponents(
                                    year=1970,
                                    month="JAN",
                                    day=15,
                                ),
                                issue_date=DateComponents(
                                    year=1970,
                                    month="JAN",
                                    day=15,
                                ),
                                issuing_country="USA",
                                issuing_state="USA_AL",
                                id_name="id_name_example",
                                issuing_agency="issuing_agency_example",
                            ),
                        ],
                        title_type="ACCOUNTING_MANAGER",
                        title="Chief Technology Officer",
                        signing_personal_guarantee=True,
                        responsible_party=True,
                        related_party=True,
                        residing_country="GBR",
                        primary_nationality="GBR",
                        secondary_nationality="IRL",
                        documentary_info=DocumentaryInfo(
                            documentary=True,
                            documentary_verifier="SALES_TEAM",
                            documentary_issuer="USA",
                            documentary_type="DRIVER_LICENSE",
                            id_number="111111117",
                            issue_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            expiry_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issuing_state="USA_AL",
                            foreign_issuing_state="foreign_issuing_state_example",
                        ),
                        alternate_address_info=AlternateAddressInfo(
                            document_needed=True,
                            document_verified=True,
                            alternate_address_document_type="BANK_STATEMENT",
                            document_name="document_name_example",
                        ),
                        is_new_owner=True,
                        directional_ownership_type="DIRECT_OWNERSHIP",
                        signing_agreement=True,
                        us_person=True,
                    ),
                ],
                contact=Person(
                    name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    contact_info=ContactInfo(
                        address=Address(
                            street_name="Baker Street",
                            street_number="221",
                            line_two="Apt B",
                            line_three="48",
                            city="Atlanta",
                            county="Fulton",
                            post_code="30346",
                            country="USA",
                            state="USA_AL",
                            classification="BUSINESS_STREET_ADDRESS",
                            contact_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            location_name="Baker Plaza",
                        ),
                        additional_addresses={
                            "key": Address(
                                street_name="Baker Street",
                                street_number="221",
                                line_two="Apt B",
                                line_three="48",
                                city="Atlanta",
                                county="Fulton",
                                post_code="30346",
                                country="USA",
                                state="USA_AL",
                                classification="BUSINESS_STREET_ADDRESS",
                                contact_name=Name(
                                    salutation="MR",
                                    first_name="John",
                                    middle_name="Lee",
                                    last_name="Doe",
                                ),
                                location_name="Baker Plaza",
                            ),
                        },
                        phone=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        mobile=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        fax=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        email_address="contactname@email.com",
                    ),
                    dob=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    positions={
                        "key": True,
                    },
                    ownership_pct="90",
                    ids=[
                        Identification(
                            id_type="PASSPORT",
                            id_number="123456789",
                            expiry_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issue_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issuing_country="USA",
                            issuing_state="USA_AL",
                            id_name="id_name_example",
                            issuing_agency="issuing_agency_example",
                        ),
                    ],
                    title_type="ACCOUNTING_MANAGER",
                    title="Chief Technology Officer",
                    signing_personal_guarantee=True,
                    responsible_party=True,
                    related_party=True,
                    residing_country="GBR",
                    primary_nationality="GBR",
                    secondary_nationality="IRL",
                    documentary_info=DocumentaryInfo(
                        documentary=True,
                        documentary_verifier="SALES_TEAM",
                        documentary_issuer="USA",
                        documentary_type="DRIVER_LICENSE",
                        id_number="111111117",
                        issue_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        expiry_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        issuing_state="USA_AL",
                        foreign_issuing_state="foreign_issuing_state_example",
                    ),
                    alternate_address_info=AlternateAddressInfo(
                        document_needed=True,
                        document_verified=True,
                        alternate_address_document_type="BANK_STATEMENT",
                        document_name="document_name_example",
                    ),
                    is_new_owner=True,
                    directional_ownership_type="DIRECT_OWNERSHIP",
                    signing_agreement=True,
                    us_person=True,
                ),
                bank_accounts={
                    "key": BankingInfo(
                        account_name="John Doe",
                        bank_name="Wells Fargo",
                        urgent_payment=True,
                        funding_method="NETCREDIT",
                        account_number="20581687",
                        sort_code="121000248",
                        iban="GB48LOYD3037341",
                        swift_code="CPRTGB22",
                        bank_creditor_id="bank_creditor_id_example",
                        bank_direct=True,
                        country="GBR",
                        tape_id="14",
                        true_daily=True,
                        use_chain_account_number=True,
                    ),
                },
                card_pricing=CardPricing(
                    pricing_method="CLEAR_AND_SIMPLE",
                    pricing_category="RETAIL",
                    amex_accepting_info=AmexAcceptingInfo(
                        amex_monthly_card_sales=3553.0,
                        is_existing=True,
                        amex_mid="2101491576",
                    ),
                    payment_facilitator_info=PaymentFacilitatorInfo(
                        payment_facilitator_type="PAYMENT_FACILITATOR",
                        card_prefixes=[
                            CardPrefix(
                                card_type="VISA",
                                prefix="DE",
                            ),
                        ],
                    ),
                    card_charges=[
                        CardCharge(
                            card_type="VISA",
                            minimum_fee=0.03,
                            authorization_fee=3.14,
                            se_number="123456789",
                            service_type="PARTIAL_SERVICE",
                            card_funding="ELAVON",
                            pricing_tiers={
                                "key": PricingTier(
                                    discount_rate=2.0,
                                    discount_per_item=0.2,
                                ),
                            },
                        ),
                    ],
                    exception_charges=[
                        ExceptionCharge(
                            type="BUSINESS_CARDS",
                            discount_rate=1.0,
                            discount_per_item=0.1,
                        ),
                    ],
                    debit_pricing=DebitPricing(
                        pricing_method="INTERCHANGE_DIFFERENTIAL",
                        authorization_method="FIXED",
                        surcharge_amount=1.1,
                        surcharge_percent="0.1",
                        debit_network_charges=[
                            DebitNetworkCharge(
                                type="INTERLINK",
                                discount_rate=5.0,
                                discount_per_item=0.5,
                                per_auth=3.14,
                            ),
                        ],
                        pinless_setup=True,
                    ),
                ),
                fees=[
                    Fee(
                        type="JOI",
                        quantity=1,
                        amount=9.99,
                        frequency="ANNUAL",
                        start_month="JAN",
                    ),
                ],
                monetary_pricing_program="monetary_pricing_program_example",
                authenticate_pricing_program="47777",
                parent_entity="parent_entity_example",
                short_name="MS00EPNA",
                fraud_check_result=FraudCheckResult(
                    transaction_id="1100000000540130",
                    decision="PASS",
                ),
                site_survey=SiteSurvey(
                    site_survey_conducted=True,
                    location_type="SHOPPING_CENTRE",
                    site_address_same_as_dba=True,
                    location_environment="BUSINESS_DISTRICT",
                    vicinity_condition="WELL_KEPT",
                    location_square_meters="LTE_TO_250",
                    location_appearance="VERY_GOOD",
                    business_operating=True,
                    inventory_display_adequate=True,
                    inventory_consistent_with_business_type=True,
                    card_decals_visible=True,
                    card_decals_installed_at_visit=True,
                ),
                dynamic_currency_conversion=DynamicCurrencyConversion(
                    rebate_percent=0.5,
                    mark_up="ZERO",
                    currency_group="FIVE_USD_DCC_CURRENCIES",
                    registration_fee=2.0,
                ),
                billing_statement=BillingStatement(
                    type="SURCHARGE_TIERED",
                    media="DYNAMIC_MERCHANT_REPORTING",
                    address_type="BUSINESS",
                    email_address="applicantname@email.com",
                    frequency="DAILY",
                ),
                funding_statement=FundingStatement(
                    type="SURCHARGE_TIERED",
                    media="DYNAMIC_MERCHANT_REPORTING",
                    email_address="applicant@email.com",
                    frequency="DAILY",
                ),
                electronic_statement=ElectronicStatement(
                    type="SURCHARGE_TIERED",
                    media="DYNAMIC_MERCHANT_REPORTING",
                    email_address="applicant@email.com",
                    frequency="DAILY",
                ),
                vat_invoice_statement=VatInvoiceStatement(
                    type="SURCHARGE_TIERED",
                    media="DYNAMIC_MERCHANT_REPORTING",
                    address_type="BUSINESS",
                ),
                billing_method="NETCREDIT",
                referrer_name="PARTNER_BANK",
                referrer_reference_number="11",
                previous_processor="previous_processor_example",
                value_added_info=ValueAddedInfo(
                    value_adds={
                        "key": True,
                    },
                    ebt_info=EbtInfo(
                        se_number="123456789",
                        authorization_fee=0.03,
                    ),
                    ecs_info=EcsInfo(
                        processing_acceptance_type="POP_POS_IMAGE",
                        service_level_type="GUARANTEE_WITH_VERIFY",
                        annual_check_volume=100000.0,
                        average_check_amount=25.0,
                        max_check_amount=1000,
                        per_transaction=0.0,
                        discount_rate=0.0,
                        monthly_minimum=0.0,
                        per_return_fee=0.0,
                        nsf_service_processing_fee=0.0,
                        nsf_service_fee=0.0,
                        collection=True,
                        enquire_reporting=True,
                        service_provider_type="ENCIRCLE_DIRECT",
                    ),
                    acs_info=AcsInfo(
                        reporting_id="reporting_id_example",
                    ),
                    fanfare_info=FanfareInfo(
                        max_card_value="max_card_value_example",
                        package_type="STANDARD_GIFT_LOYALTY",
                        enrollment={
                            "key": EnrollmentInfo(
                                discount_rate=0.0,
                                discount_amount=0.0,
                            ),
                        },
                        loyalty={
                            "key": LoyaltyInfo(
                                visits=1,
                                amount_spent=22.0,
                                discount_rate=1.1,
                                discount_amount=5.0,
                            ),
                        },
                    ),
                    gsm_prepaid_type="EURONET_NO_PAYS",
                    surcharge_managed_by="surcharge_managed_by_example",
                    credit_surcharge_amt="credit_surcharge_amt_example",
                    efs3d_secure_info=Efs3dSecureInfo(
                        billing_per_item_fee=3.14,
                    ),
                    straight_send_info=StraightSendInfo(
                        per_transaction_fee=3.14,
                        percent_fee=3.14,
                    ),
                    on_demand_info=OnDemandInfo(
                        per_transaction_fee=3.14,
                        percent_fee=3.14,
                    ),
                    ocm_info=OcmInfo(
                        setup_type="Mid, Chain",
                        setup_fee=0.0,
                        monthly_fee=0.0,
                        number_of_users=1,
                    ),
                ),
                equipment_info=EquipmentInfo(
                    equipment_items=[
                        EquipmentItem(
                            code="310T3",
                            quantity=2,
                            pricing_items=[
                                EquipmentPricing(
                                    amount=200.0,
                                    purchase_type="EXCHANGE",
                                    lease_term=1,
                                    vendor_code=1,
                                    vendor_plan="vendor_plan_example",
                                    start_month="JAN",
                                    start_year="2010",
                                ),
                            ],
                            item_settings=ItemSettings(
                                security_level="BASIC",
                                semi_integrated=True,
                                connection_type="STANDARD_IP",
                                close_method="MANUAL",
                                capture_method="HOST",
                                qir_vendor="qir_vendor_example",
                                services={
                                    "key": True,
                                },
                                options=[
                                    EquipmentOption(
                                        integrator_code="integrator_code_example",
                                        ciers_number="ciers_number_example",
                                        serial_number="serial_number_example",
                                        model_number="model_number_example",
                                        ecr_type="SMARTLINK",
                                        ecr_mode="LITE_TOUCH",
                                        print_via_ecr=True,
                                        ecr_integrator="ALMAR",
                                        ecr_cable_type="NONE",
                                        epg_integration_type="REMOTE",
                                        bax_number="bax_number_example",
                                        bax_effective_date=DateComponents(
                                            year=1970,
                                            month="JAN",
                                            day=15,
                                        ),
                                    ),
                                ],
                                bundled_thresh_hold=1,
                                service_pricing_code="CORE",
                                terminal_type="INTERNET",
                                ingenico_pay_table=True,
                                deploy_type="DEPLOY",
                            ),
                            exception_items=[
                                ExceptionItem(
                                    type="type_example",
                                    discount_rate=3.14,
                                    discount_per_item=3.14,
                                ),
                            ],
                            service_fee=3.14,
                            trx_free_month=1,
                            future_effective_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                        ),
                    ],
                    terminal_services=[
                        TerminalService(
                            type="QUICK_CLOSE",
                            service_specifics="service_specifics_example",
                        ),
                    ],
                    training_type="TRAINING",
                    shipping_method="NEXT_DAY",
                    network="ELAVON",
                    fusebox_info=FuseboxInfo(
                        simplify_quantity=1,
                        direct_quantity=1,
                        simplify_location="simplify_location_example",
                        direct_to_fusebox_location="direct_to_fusebox_location_example",
                    ),
                    anticipated_start_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                ),
                branch_number="111",
                branch_code="1234",
                self_boarded_external=True,
                employee_number="11222",
                rep_referral_number="321",
                promotional_code="00001",
                chain_info=ChainInfo(
                    chain_number="chain_number_example",
                    chain_name="chain_name_example",
                    send_statement_to_address="BUSINESS",
                    statement_media="DYNAMIC_MERCHANT_REPORTING",
                    address=Address(
                        street_name="Baker Street",
                        street_number="221",
                        line_two="Apt B",
                        line_three="48",
                        city="Atlanta",
                        county="Fulton",
                        post_code="30346",
                        country="USA",
                        state="USA_AL",
                        classification="BUSINESS_STREET_ADDRESS",
                        contact_name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        location_name="Baker Plaza",
                    ),
                    chain_level_billing=True,
                    bank_accounts={
                        "key": BankingInfo(
                            account_name="John Doe",
                            bank_name="Wells Fargo",
                            urgent_payment=True,
                            funding_method="NETCREDIT",
                            account_number="20581687",
                            sort_code="121000248",
                            iban="GB48LOYD3037341",
                            swift_code="CPRTGB22",
                            bank_creditor_id="bank_creditor_id_example",
                            bank_direct=True,
                            country="GBR",
                            tape_id="14",
                            true_daily=True,
                            use_chain_account_number=True,
                        ),
                    },
                ),
                distributions={
                    "key": DistributionInfo(
                        method="MAILING",
                        address_type="BUSINESS",
                        email_address="applicant@email.com",
                    ),
                },
                additional_location_info=AdditionalLocationInfo(
                    central_mid="8024999222",
                    central_legal_name="Elavon",
                    central_tax_id="787421357",
                ),
                signed_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                signed_type="WET",
                intermediary_owner_info=IntermediaryOwnerInfo(
                    intermediary_owners=[
                        IntermediaryOwner(
                            ownership_pct="90",
                            business_name="ACME",
                            owner_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            phone=PhoneNumber(
                                intl_code="44",
                                area_code="111",
                                number="1231234",
                                extension="2",
                            ),
                            email_address="email_address_example",
                            address=Address(
                                street_name="Baker Street",
                                street_number="221",
                                line_two="Apt B",
                                line_three="48",
                                city="Atlanta",
                                county="Fulton",
                                post_code="30346",
                                country="USA",
                                state="USA_AL",
                                classification="BUSINESS_STREET_ADDRESS",
                                contact_name=Name(
                                    salutation="MR",
                                    first_name="John",
                                    middle_name="Lee",
                                    last_name="Doe",
                                ),
                                location_name="Baker Plaza",
                            ),
                        ),
                    ],
                    additional_intermediate_owners=True,
                ),
                revenue_share_info=RevenueShareInfo(
                    secondary_sales_person="12345",
                    split_percentage="50",
                ),
                elavon_contract="UK",
                internal_use_info=InternalUseInfo(
                    field_auto_info=FieldAutoInfo(
                        requested=True,
                        applied=True,
                        monitored=True,
                        values_modified=True,
                        field_auto_reference_id="field_auto_reference_id_example",
                    ),
                    sales_rep_info=SalesRepInfo(
                        sales_rep_code="12345",
                        name="name_example",
                        email="repname@email.com",
                        submitted=True,
                    ),
                    tin_applied_to_all=True,
                    ip_address="ip_address_example",
                ),
                eframe_info=EframeInfo(
                    scheme_selection="scheme_selection_example",
                    pos_contract=True,
                    is_girocard=True,
                ),
                partner_info=PartnerInfo(
                    partner_name="partner_name_example",
                    associate_id="associate_id_example",
                    book_of_business="book_of_business_example",
                    correlation_id="correlation_id_example",
                    partner_source="partner_source_example",
                    merchant_user_id="merchant_user_id_example",
                    session_id="session_id_example",
                ),
                alternative_payment_methods=[
                    ApmAcquirer(
                        acquirer_code="acquirer_code_example",
                        acquirer_types=[
                            ApmAcquirerType(
                                type_code="type_code_example",
                                per_item_amount="per_item_amount_example",
                                rate_percentage="rate_percentage_example",
                                pricing_tiers=[
                                    ApmPricingTier(
                                        combining_code="combining_code_example",
                                        per_item_amount="per_item_amount_example",
                                        rate_percentage="rate_percentage_example",
                                        description="description_example",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            language="language_example",
            agreement_id="agreement_id_example",
            is_grouped_application=True,
            wet_signed=True,
            card_volume=CardVolume(
                visa_percentage="15.6",
                master_card_percentage="12.3",
                amex_percentage="4.5",
                amex_average_transaction="10.1",
                interac_average_transaction="23.4",
            ),
            vendor_info=ProviderInfo(
                representative_name="Alex Smith",
                representative_email="asmith@email.com",
                representative_sales_code="12345",
                representative_contact_number=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
            ),
            acting_intermediary_info=ActingIntermediaryInfo(
                acting_intermediary_name="acting_intermediary_name_example",
                acting_intermediary_type="QUALIFIED_INTERMEDIARY",
            ),
            bank_account_details_map={
                "key": BankAccountAdditionalInfo(
                    bank_name="bank_name_example",
                    bank_branch="bank_branch_example",
                    direct_debit_authorized=True,
                ),
            },
            is_tax_exempt_equipment=True,
            talech_egift_only=True,
            displayed_currency="displayed_currency_example",
            additional_description_info=AdditionalDescriptionInfo(
                previous_processor_description="Bank of America",
                monetary_pricing_program_description="MIF Unblended",
                referrer_reference_description="referrer_reference_description_example",
                notes="notes_example",
            ),
            additional_value_added_service_info=ValueAddedServices(
                ecs=ElectronicCheckService(
                    reporting_fee=3.14,
                    reporting_num_users="reporting_num_users_example",
                    ach_check_questions=AchCheckQuestions(
                        payment_acceptance_type="payment_acceptance_type_example",
                        prior_acceptance_authorization=True,
                        customer_identification=True,
                        ach_customer_type="EXISTING",
                        maintain_and_disclose_cancel=True,
                        ensure_accurate_transaction_info=True,
                    ),
                ),
                fanfare=Fanfare(
                    setup_fee=1.1,
                    monthly_fee=0.06,
                    annual_fee=1.6,
                    custom_card_upgrade_fee=0.02,
                    included_cards=FanfareCardSplits(
                        promotional="promotional_example",
                        loyalty="loyalty_example",
                        gift="gift_example",
                    ),
                    additional_cards_type="FF_STANDARD",
                    additional_cards=FanfareCardSplits(
                        promotional="promotional_example",
                        loyalty="loyalty_example",
                        gift="gift_example",
                    ),
                    additional_card_price=3.14,
                    program_checkup=3.14,
                    card_style="card_style_example",
                    justification_type="LEFT",
                    card_is_text=True,
                    card_text="card_text_example",
                    text_case_type="TITLE_CASE",
                    text_color="text_color_example",
                    text_font="text_font_example",
                ),
            ),
            additional_business_info=AdditionalBusinessInfo(
                ownership_years_over_range="3",
                is_max_establishment_year=True,
                has_government_incentive=True,
            ),
            funding_type="STANDARD",
            integrator_solution_info=IntegratorSolutionInfo(
                health_care_eligibility_selection_map={
                    "key": HealthCareEligibilityInfo(
                        monthly_fee=0.0,
                        npi_numbers=[
                            "npi_numbers_example",
                        ],
                    ),
                },
                payments=Payments(
                    pms_vendor_pas="pms_vendor_pas_example",
                    number_of_providers="1",
                    sales_rep_phone_number="sales_rep_phone_number_example",
                    integrator_notes="1111111111",
                    has_payment_plans=True,
                ),
                has_ecs_only=True,
                sku="310T3",
            ),
            additional_lease_info=AdditionalLeaseInfo(
                lease_details_map={
                    "key": LeaseDetails(
                        alternate_price=3.14,
                        pricing_plan="pricing_plan_example",
                    ),
                },
            ),
            marketing_data_consent_map={
                "key": True,
            },
            additional_site_survey_info=AdditionalSiteSurveyInfo(
                incomplete_survey_reason_type="NOT_OPEN",
                site_survey_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                site_survey_conducted_by="site_survey_conducted_by_example",
                description_of_no_site_survey="description_of_no_site_survey_example",
            ),
            kyc_quiz_status_map={
                "KYC_RESULT_FAILED_QUIZ": "KYC_RESULT_FAILED_QUIZ",
            },
            var_other_details=VarOtherDetails(
                var_type="VENDOR_DISTRIBUTED",
                vendor="vendor_example",
                product="product_example",
                version="version_example",
            ),
            additional_card_pricing_info=AdditionalCardPricingInfo(
                minimum_card_fee=0.0,
                clear_and_simple_type="clear_and_simple_type_example",
                c4_pricing_type="c4_pricing_type_example",
                high_risk_cost_additional_loading="high_risk_cost_additional_loading_example",
            ),
            sales_office_contact=SalesOfficeContact(
                address=Address(
                    street_name="Baker Street",
                    street_number="221",
                    line_two="Apt B",
                    line_three="48",
                    city="Atlanta",
                    county="Fulton",
                    post_code="30346",
                    country="USA",
                    state="USA_AL",
                    classification="BUSINESS_STREET_ADDRESS",
                    contact_name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    location_name="Baker Plaza",
                ),
                phone=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
            ),
            sales_person_contact=SalesPersonContact(
                name=Name(
                    salutation="MR",
                    first_name="John",
                    middle_name="Lee",
                    last_name="Doe",
                ),
                phone=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                email_address="email_address_example",
            ),
            additional_auth_pricing_program_info=AdditionalAuthPricingProgramInfo(
                description="description_example",
                fee=5.0,
                auth_amount=10.0,
            ),
            applicant_email="applicant_email_example",
            partner_document_data={
                "key": {
                    "key": "key_example",
                },
            },
            application_id=1,
        ),
    ) # AppendGroupDocumentPacketRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Append to Group Document Packet
        api_response = api_instance.append_group_document_packet(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->append_group_document_packet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppendGroupDocumentPacketRequest**](AppendGroupDocumentPacketRequest.md)|  |

### Return type

[**AppendGroupDocumentPacketResponse**](AppendGroupDocumentPacketResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Append Group Document Packet Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_validate**
> VerifyBankAccountResponse bank_validate(version_number, body)

Validate Bank Account

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.verify_bank_account_response import VerifyBankAccountResponse
from elavon.model.banking_info import BankingInfo
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    version_number = 1 # int | 
    body = BankingInfo(
        account_name="John Doe",
        bank_name="Wells Fargo",
        urgent_payment=True,
        funding_method="NETCREDIT",
        account_number="20581687",
        sort_code="121000248",
        iban="GB48LOYD3037341",
        swift_code="CPRTGB22",
        bank_creditor_id="bank_creditor_id_example",
        bank_direct=True,
        country="GBR",
        tape_id="14",
        true_daily=True,
        use_chain_account_number=True,
    ) # BankingInfo | 

    # example passing only required values which don't have defaults set
    try:
        # Validate Bank Account
        api_response = api_instance.bank_validate(version_number, body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->bank_validate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_number** | **int**|  |
 **body** | [**BankingInfo**](BankingInfo.md)|  |

### Return type

[**VerifyBankAccountResponse**](VerifyBankAccountResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Verify Bank Account Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_xsd_schema**
> bank_xsd_schema(version_number)

Get Bank Account Validation Schema

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    version_number = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get Bank Account Validation Schema
        api_instance.bank_xsd_schema(version_number)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->bank_xsd_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_number** | **int**|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **board**
> BoardingResponse board(version_number, body)

Boarding

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.boarding_request_params import BoardingRequestParams
from elavon.model.boarding_response import BoardingResponse
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    version_number = 1 # int | 
    body = BoardingRequestParams(
        credit_check_token="credit_check_token_example",
        group_info=GroupInfo(
            group_id="group_id_example",
            sequence_number=1,
            total_number=1,
        ),
        scarecrow_application=ScarecrowApplication(
            client_id="IDNA",
            client_group_number="860",
            unique_id="AcmeCorp1572566399123",
            banker_id="123",
            banker_partner_id="123",
            country="USA",
            principal=Person(
                name=Name(
                    salutation="MR",
                    first_name="John",
                    middle_name="Lee",
                    last_name="Doe",
                ),
                contact_info=ContactInfo(
                    address=Address(
                        street_name="Baker Street",
                        street_number="221",
                        line_two="Apt B",
                        line_three="48",
                        city="Atlanta",
                        county="Fulton",
                        post_code="30346",
                        country="USA",
                        state="USA_AL",
                        classification="BUSINESS_STREET_ADDRESS",
                        contact_name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        location_name="Baker Plaza",
                    ),
                    additional_addresses={
                        "key": Address(
                            street_name="Baker Street",
                            street_number="221",
                            line_two="Apt B",
                            line_three="48",
                            city="Atlanta",
                            county="Fulton",
                            post_code="30346",
                            country="USA",
                            state="USA_AL",
                            classification="BUSINESS_STREET_ADDRESS",
                            contact_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            location_name="Baker Plaza",
                        ),
                    },
                    phone=PhoneNumber(
                        intl_code="44",
                        area_code="111",
                        number="1231234",
                        extension="2",
                    ),
                    mobile=PhoneNumber(
                        intl_code="44",
                        area_code="111",
                        number="1231234",
                        extension="2",
                    ),
                    fax=PhoneNumber(
                        intl_code="44",
                        area_code="111",
                        number="1231234",
                        extension="2",
                    ),
                    email_address="contactname@email.com",
                ),
                dob=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                positions={
                    "key": True,
                },
                ownership_pct="90",
                ids=[
                    Identification(
                        id_type="PASSPORT",
                        id_number="123456789",
                        expiry_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        issue_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        issuing_country="USA",
                        issuing_state="USA_AL",
                        id_name="id_name_example",
                        issuing_agency="issuing_agency_example",
                    ),
                ],
                title_type="ACCOUNTING_MANAGER",
                title="Chief Technology Officer",
                signing_personal_guarantee=True,
                responsible_party=True,
                related_party=True,
                residing_country="GBR",
                primary_nationality="GBR",
                secondary_nationality="IRL",
                documentary_info=DocumentaryInfo(
                    documentary=True,
                    documentary_verifier="SALES_TEAM",
                    documentary_issuer="USA",
                    documentary_type="DRIVER_LICENSE",
                    id_number="111111117",
                    issue_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    expiry_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    issuing_state="USA_AL",
                    foreign_issuing_state="foreign_issuing_state_example",
                ),
                alternate_address_info=AlternateAddressInfo(
                    document_needed=True,
                    document_verified=True,
                    alternate_address_document_type="BANK_STATEMENT",
                    document_name="document_name_example",
                ),
                is_new_owner=True,
                directional_ownership_type="DIRECT_OWNERSHIP",
                signing_agreement=True,
                us_person=True,
            ),
            business_info=BusinessInfo(
                dba_name="Grimm's Bookstore",
                dba_name_extended="Grimm's Fairytales and Other Stories Bookstore",
                business_address=Address(
                    street_name="Baker Street",
                    street_number="221",
                    line_two="Apt B",
                    line_three="48",
                    city="Atlanta",
                    county="Fulton",
                    post_code="30346",
                    country="USA",
                    state="USA_AL",
                    classification="BUSINESS_STREET_ADDRESS",
                    contact_name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    location_name="Baker Plaza",
                ),
                legal_name="Barkers Dog Bakery",
                legal_name_extended="Baking Better Biscuits for Your Favorite Barkers Dog Bakery LLC",
                legal_name_marked=[
                    "legal_name_marked_example",
                ],
                additional_addresses={
                    "key": Address(
                        street_name="Baker Street",
                        street_number="221",
                        line_two="Apt B",
                        line_three="48",
                        city="Atlanta",
                        county="Fulton",
                        post_code="30346",
                        country="USA",
                        state="USA_AL",
                        classification="BUSINESS_STREET_ADDRESS",
                        contact_name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        location_name="Baker Plaza",
                    ),
                },
                ownership_type="SOLE_TRADER",
                registration_number="1234567",
                tax_id="787421357",
                tax_id_type="FEDERAL_TAX_ID",
                vat_info=VatInfo(
                    number_option="VAT_NBR",
                    number56_b="123456789",
                    expiry_date56_b=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    tax_number_type="CORPORATE_TAX_NUMBER",
                    tax_number="tax_number_example",
                ),
                tax_form_type="W9",
                tax_class_type="CORPORATION",
                customer_membership_number="111222",
                product_description="Bakeries",
                mcc_code="7399E",
                establishment_year="2005",
                current_ownership_years="3",
                current_ownership_months="6",
                government_owned_entity=True,
                communication_language="en",
                pos_language="en",
                store_number="123456789",
                association_codes=[
                    "12345",
                ],
                opt_out=True,
                sign_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                pci_info=PCIInfo(
                    pci_program_level="ONE",
                    pci_service_type="BASIC",
                    pci_contact_first_name="pci_contact_first_name_example",
                    pci_contact_last_name="pci_contact_last_name_example",
                    pci_contact_email_address="pci_contact_email_address_example",
                    pci_contact_phone=PhoneNumber(
                        intl_code="44",
                        area_code="111",
                        number="1231234",
                        extension="2",
                    ),
                    pci_groups=[
                        "PCI_PROGRAM_EXCLUSION",
                    ],
                ),
                employer_id="1234567",
                country_of_origin="USA",
                exemption_type="ADDITIONAL_LOCATION",
                owner_exemption_type="BANK_ADVISED_POOLED",
                number_of_partners="ONE",
                relationship_mgr_code="1234567",
                country_of_primary_operation="USA",
                bearer_shares=True,
                legal_status="CERTIFIED_INCORPORATION_ARTICLES",
                verifications={
                    "key": VerificationInfo(
                        documentary=True,
                        issuing_country="USA",
                        issuing_state="USA_AL",
                        site_person_met="John Smith",
                        site_visit_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        id_number="111111117",
                        issue_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        expiry_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        document_type="CERTIFIED_INCORPORATION_ARTICLES",
                    ),
                },
                industry_class="LODGING",
                no_plates=True,
                agent_number="1223334",
                location_mid_range="NORDIC",
                hemp_grower_info=HempGrowerInfo(
                    operations_description="operations_description_example",
                    is_licensed=True,
                    license_expiration_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    additional_mrb_activity=True,
                    cannabis_revenue_percentage_range="NONE",
                ),
                credit_decision_info=CreditDecisionInfo(
                    credit_decision_flag=True,
                    credit_decision_id="credit_decision_id_example",
                ),
            ),
            financial_info=FinancialInfo(
                avg_sale_amount="125",
                monthly_card_sales="1000",
                annual_card_sales="12000",
                annual_revenue="240000",
                highest_ticket_amount="1000",
                highest_ticket_frequency=1,
                funding_currency="USD",
                card_present_acceptance_percent="100",
                internet_acceptance_percent="0",
                moto_acceptance_percent="0",
                business_email_address="business_email_address_example",
                business_website_url="business@email.com",
                customer_service_phone=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                not_present_delay_days=0,
                deposit_frequency="0",
                deposit_size_percent="1",
                deposit_balance_days="1",
                deposit_fulfillment_days="1",
                full_payment_percent="1",
                full_payment_fulfillment="1",
                utilize_cvv2=True,
                recurring_transactions=True,
                contract_term_type="ZERO_MONTH",
                months_closed=[
                    "JAN",
                ],
                monetary_billing_method="CARD_DISCOUNT",
                authorization_included=True,
                annual_fee_month_start="JAN",
                money_services=True,
                payment_services=True,
                third_party_processor=True,
                non_government_non_profit=True,
                daily_discount=True,
                non_bank_atm=True,
                embassy=True,
                high_inter_annual_trans_ngo=True,
            ),
            sales_rep_code="12345",
            additional_shareholders=[
                Person(
                    name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    contact_info=ContactInfo(
                        address=Address(
                            street_name="Baker Street",
                            street_number="221",
                            line_two="Apt B",
                            line_three="48",
                            city="Atlanta",
                            county="Fulton",
                            post_code="30346",
                            country="USA",
                            state="USA_AL",
                            classification="BUSINESS_STREET_ADDRESS",
                            contact_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            location_name="Baker Plaza",
                        ),
                        additional_addresses={
                            "key": Address(
                                street_name="Baker Street",
                                street_number="221",
                                line_two="Apt B",
                                line_three="48",
                                city="Atlanta",
                                county="Fulton",
                                post_code="30346",
                                country="USA",
                                state="USA_AL",
                                classification="BUSINESS_STREET_ADDRESS",
                                contact_name=Name(
                                    salutation="MR",
                                    first_name="John",
                                    middle_name="Lee",
                                    last_name="Doe",
                                ),
                                location_name="Baker Plaza",
                            ),
                        },
                        phone=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        mobile=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        fax=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        email_address="contactname@email.com",
                    ),
                    dob=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    positions={
                        "key": True,
                    },
                    ownership_pct="90",
                    ids=[
                        Identification(
                            id_type="PASSPORT",
                            id_number="123456789",
                            expiry_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issue_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issuing_country="USA",
                            issuing_state="USA_AL",
                            id_name="id_name_example",
                            issuing_agency="issuing_agency_example",
                        ),
                    ],
                    title_type="ACCOUNTING_MANAGER",
                    title="Chief Technology Officer",
                    signing_personal_guarantee=True,
                    responsible_party=True,
                    related_party=True,
                    residing_country="GBR",
                    primary_nationality="GBR",
                    secondary_nationality="IRL",
                    documentary_info=DocumentaryInfo(
                        documentary=True,
                        documentary_verifier="SALES_TEAM",
                        documentary_issuer="USA",
                        documentary_type="DRIVER_LICENSE",
                        id_number="111111117",
                        issue_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        expiry_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        issuing_state="USA_AL",
                        foreign_issuing_state="foreign_issuing_state_example",
                    ),
                    alternate_address_info=AlternateAddressInfo(
                        document_needed=True,
                        document_verified=True,
                        alternate_address_document_type="BANK_STATEMENT",
                        document_name="document_name_example",
                    ),
                    is_new_owner=True,
                    directional_ownership_type="DIRECT_OWNERSHIP",
                    signing_agreement=True,
                    us_person=True,
                ),
            ],
            contact=Person(
                name=Name(
                    salutation="MR",
                    first_name="John",
                    middle_name="Lee",
                    last_name="Doe",
                ),
                contact_info=ContactInfo(
                    address=Address(
                        street_name="Baker Street",
                        street_number="221",
                        line_two="Apt B",
                        line_three="48",
                        city="Atlanta",
                        county="Fulton",
                        post_code="30346",
                        country="USA",
                        state="USA_AL",
                        classification="BUSINESS_STREET_ADDRESS",
                        contact_name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        location_name="Baker Plaza",
                    ),
                    additional_addresses={
                        "key": Address(
                            street_name="Baker Street",
                            street_number="221",
                            line_two="Apt B",
                            line_three="48",
                            city="Atlanta",
                            county="Fulton",
                            post_code="30346",
                            country="USA",
                            state="USA_AL",
                            classification="BUSINESS_STREET_ADDRESS",
                            contact_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            location_name="Baker Plaza",
                        ),
                    },
                    phone=PhoneNumber(
                        intl_code="44",
                        area_code="111",
                        number="1231234",
                        extension="2",
                    ),
                    mobile=PhoneNumber(
                        intl_code="44",
                        area_code="111",
                        number="1231234",
                        extension="2",
                    ),
                    fax=PhoneNumber(
                        intl_code="44",
                        area_code="111",
                        number="1231234",
                        extension="2",
                    ),
                    email_address="contactname@email.com",
                ),
                dob=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                positions={
                    "key": True,
                },
                ownership_pct="90",
                ids=[
                    Identification(
                        id_type="PASSPORT",
                        id_number="123456789",
                        expiry_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        issue_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        issuing_country="USA",
                        issuing_state="USA_AL",
                        id_name="id_name_example",
                        issuing_agency="issuing_agency_example",
                    ),
                ],
                title_type="ACCOUNTING_MANAGER",
                title="Chief Technology Officer",
                signing_personal_guarantee=True,
                responsible_party=True,
                related_party=True,
                residing_country="GBR",
                primary_nationality="GBR",
                secondary_nationality="IRL",
                documentary_info=DocumentaryInfo(
                    documentary=True,
                    documentary_verifier="SALES_TEAM",
                    documentary_issuer="USA",
                    documentary_type="DRIVER_LICENSE",
                    id_number="111111117",
                    issue_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    expiry_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    issuing_state="USA_AL",
                    foreign_issuing_state="foreign_issuing_state_example",
                ),
                alternate_address_info=AlternateAddressInfo(
                    document_needed=True,
                    document_verified=True,
                    alternate_address_document_type="BANK_STATEMENT",
                    document_name="document_name_example",
                ),
                is_new_owner=True,
                directional_ownership_type="DIRECT_OWNERSHIP",
                signing_agreement=True,
                us_person=True,
            ),
            bank_accounts={
                "key": BankingInfo(
                    account_name="John Doe",
                    bank_name="Wells Fargo",
                    urgent_payment=True,
                    funding_method="NETCREDIT",
                    account_number="20581687",
                    sort_code="121000248",
                    iban="GB48LOYD3037341",
                    swift_code="CPRTGB22",
                    bank_creditor_id="bank_creditor_id_example",
                    bank_direct=True,
                    country="GBR",
                    tape_id="14",
                    true_daily=True,
                    use_chain_account_number=True,
                ),
            },
            card_pricing=CardPricing(
                pricing_method="CLEAR_AND_SIMPLE",
                pricing_category="RETAIL",
                amex_accepting_info=AmexAcceptingInfo(
                    amex_monthly_card_sales=3553.0,
                    is_existing=True,
                    amex_mid="2101491576",
                ),
                payment_facilitator_info=PaymentFacilitatorInfo(
                    payment_facilitator_type="PAYMENT_FACILITATOR",
                    card_prefixes=[
                        CardPrefix(
                            card_type="VISA",
                            prefix="DE",
                        ),
                    ],
                ),
                card_charges=[
                    CardCharge(
                        card_type="VISA",
                        minimum_fee=0.03,
                        authorization_fee=3.14,
                        se_number="123456789",
                        service_type="PARTIAL_SERVICE",
                        card_funding="ELAVON",
                        pricing_tiers={
                            "key": PricingTier(
                                discount_rate=2.0,
                                discount_per_item=0.2,
                            ),
                        },
                    ),
                ],
                exception_charges=[
                    ExceptionCharge(
                        type="BUSINESS_CARDS",
                        discount_rate=1.0,
                        discount_per_item=0.1,
                    ),
                ],
                debit_pricing=DebitPricing(
                    pricing_method="INTERCHANGE_DIFFERENTIAL",
                    authorization_method="FIXED",
                    surcharge_amount=1.1,
                    surcharge_percent="0.1",
                    debit_network_charges=[
                        DebitNetworkCharge(
                            type="INTERLINK",
                            discount_rate=5.0,
                            discount_per_item=0.5,
                            per_auth=3.14,
                        ),
                    ],
                    pinless_setup=True,
                ),
            ),
            fees=[
                Fee(
                    type="JOI",
                    quantity=1,
                    amount=9.99,
                    frequency="ANNUAL",
                    start_month="JAN",
                ),
            ],
            monetary_pricing_program="monetary_pricing_program_example",
            authenticate_pricing_program="47777",
            parent_entity="parent_entity_example",
            short_name="MS00EPNA",
            fraud_check_result=FraudCheckResult(
                transaction_id="1100000000540130",
                decision="PASS",
            ),
            site_survey=SiteSurvey(
                site_survey_conducted=True,
                location_type="SHOPPING_CENTRE",
                site_address_same_as_dba=True,
                location_environment="BUSINESS_DISTRICT",
                vicinity_condition="WELL_KEPT",
                location_square_meters="LTE_TO_250",
                location_appearance="VERY_GOOD",
                business_operating=True,
                inventory_display_adequate=True,
                inventory_consistent_with_business_type=True,
                card_decals_visible=True,
                card_decals_installed_at_visit=True,
            ),
            dynamic_currency_conversion=DynamicCurrencyConversion(
                rebate_percent=0.5,
                mark_up="ZERO",
                currency_group="FIVE_USD_DCC_CURRENCIES",
                registration_fee=2.0,
            ),
            billing_statement=BillingStatement(
                type="SURCHARGE_TIERED",
                media="DYNAMIC_MERCHANT_REPORTING",
                address_type="BUSINESS",
                email_address="applicantname@email.com",
                frequency="DAILY",
            ),
            funding_statement=FundingStatement(
                type="SURCHARGE_TIERED",
                media="DYNAMIC_MERCHANT_REPORTING",
                email_address="applicant@email.com",
                frequency="DAILY",
            ),
            electronic_statement=ElectronicStatement(
                type="SURCHARGE_TIERED",
                media="DYNAMIC_MERCHANT_REPORTING",
                email_address="applicant@email.com",
                frequency="DAILY",
            ),
            vat_invoice_statement=VatInvoiceStatement(
                type="SURCHARGE_TIERED",
                media="DYNAMIC_MERCHANT_REPORTING",
                address_type="BUSINESS",
            ),
            billing_method="NETCREDIT",
            referrer_name="PARTNER_BANK",
            referrer_reference_number="11",
            previous_processor="previous_processor_example",
            value_added_info=ValueAddedInfo(
                value_adds={
                    "key": True,
                },
                ebt_info=EbtInfo(
                    se_number="123456789",
                    authorization_fee=0.03,
                ),
                ecs_info=EcsInfo(
                    processing_acceptance_type="POP_POS_IMAGE",
                    service_level_type="GUARANTEE_WITH_VERIFY",
                    annual_check_volume=100000.0,
                    average_check_amount=25.0,
                    max_check_amount=1000,
                    per_transaction=0.0,
                    discount_rate=0.0,
                    monthly_minimum=0.0,
                    per_return_fee=0.0,
                    nsf_service_processing_fee=0.0,
                    nsf_service_fee=0.0,
                    collection=True,
                    enquire_reporting=True,
                    service_provider_type="ENCIRCLE_DIRECT",
                ),
                acs_info=AcsInfo(
                    reporting_id="reporting_id_example",
                ),
                fanfare_info=FanfareInfo(
                    max_card_value="max_card_value_example",
                    package_type="STANDARD_GIFT_LOYALTY",
                    enrollment={
                        "key": EnrollmentInfo(
                            discount_rate=0.0,
                            discount_amount=0.0,
                        ),
                    },
                    loyalty={
                        "key": LoyaltyInfo(
                            visits=1,
                            amount_spent=22.0,
                            discount_rate=1.1,
                            discount_amount=5.0,
                        ),
                    },
                ),
                gsm_prepaid_type="EURONET_NO_PAYS",
                surcharge_managed_by="surcharge_managed_by_example",
                credit_surcharge_amt="credit_surcharge_amt_example",
                efs3d_secure_info=Efs3dSecureInfo(
                    billing_per_item_fee=3.14,
                ),
                straight_send_info=StraightSendInfo(
                    per_transaction_fee=3.14,
                    percent_fee=3.14,
                ),
                on_demand_info=OnDemandInfo(
                    per_transaction_fee=3.14,
                    percent_fee=3.14,
                ),
                ocm_info=OcmInfo(
                    setup_type="Mid, Chain",
                    setup_fee=0.0,
                    monthly_fee=0.0,
                    number_of_users=1,
                ),
            ),
            equipment_info=EquipmentInfo(
                equipment_items=[
                    EquipmentItem(
                        code="310T3",
                        quantity=2,
                        pricing_items=[
                            EquipmentPricing(
                                amount=200.0,
                                purchase_type="EXCHANGE",
                                lease_term=1,
                                vendor_code=1,
                                vendor_plan="vendor_plan_example",
                                start_month="JAN",
                                start_year="2010",
                            ),
                        ],
                        item_settings=ItemSettings(
                            security_level="BASIC",
                            semi_integrated=True,
                            connection_type="STANDARD_IP",
                            close_method="MANUAL",
                            capture_method="HOST",
                            qir_vendor="qir_vendor_example",
                            services={
                                "key": True,
                            },
                            options=[
                                EquipmentOption(
                                    integrator_code="integrator_code_example",
                                    ciers_number="ciers_number_example",
                                    serial_number="serial_number_example",
                                    model_number="model_number_example",
                                    ecr_type="SMARTLINK",
                                    ecr_mode="LITE_TOUCH",
                                    print_via_ecr=True,
                                    ecr_integrator="ALMAR",
                                    ecr_cable_type="NONE",
                                    epg_integration_type="REMOTE",
                                    bax_number="bax_number_example",
                                    bax_effective_date=DateComponents(
                                        year=1970,
                                        month="JAN",
                                        day=15,
                                    ),
                                ),
                            ],
                            bundled_thresh_hold=1,
                            service_pricing_code="CORE",
                            terminal_type="INTERNET",
                            ingenico_pay_table=True,
                            deploy_type="DEPLOY",
                        ),
                        exception_items=[
                            ExceptionItem(
                                type="type_example",
                                discount_rate=3.14,
                                discount_per_item=3.14,
                            ),
                        ],
                        service_fee=3.14,
                        trx_free_month=1,
                        future_effective_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                    ),
                ],
                terminal_services=[
                    TerminalService(
                        type="QUICK_CLOSE",
                        service_specifics="service_specifics_example",
                    ),
                ],
                training_type="TRAINING",
                shipping_method="NEXT_DAY",
                network="ELAVON",
                fusebox_info=FuseboxInfo(
                    simplify_quantity=1,
                    direct_quantity=1,
                    simplify_location="simplify_location_example",
                    direct_to_fusebox_location="direct_to_fusebox_location_example",
                ),
                anticipated_start_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
            ),
            branch_number="111",
            branch_code="1234",
            self_boarded_external=True,
            employee_number="11222",
            rep_referral_number="321",
            promotional_code="00001",
            chain_info=ChainInfo(
                chain_number="chain_number_example",
                chain_name="chain_name_example",
                send_statement_to_address="BUSINESS",
                statement_media="DYNAMIC_MERCHANT_REPORTING",
                address=Address(
                    street_name="Baker Street",
                    street_number="221",
                    line_two="Apt B",
                    line_three="48",
                    city="Atlanta",
                    county="Fulton",
                    post_code="30346",
                    country="USA",
                    state="USA_AL",
                    classification="BUSINESS_STREET_ADDRESS",
                    contact_name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    location_name="Baker Plaza",
                ),
                chain_level_billing=True,
                bank_accounts={
                    "key": BankingInfo(
                        account_name="John Doe",
                        bank_name="Wells Fargo",
                        urgent_payment=True,
                        funding_method="NETCREDIT",
                        account_number="20581687",
                        sort_code="121000248",
                        iban="GB48LOYD3037341",
                        swift_code="CPRTGB22",
                        bank_creditor_id="bank_creditor_id_example",
                        bank_direct=True,
                        country="GBR",
                        tape_id="14",
                        true_daily=True,
                        use_chain_account_number=True,
                    ),
                },
            ),
            distributions={
                "key": DistributionInfo(
                    method="MAILING",
                    address_type="BUSINESS",
                    email_address="applicant@email.com",
                ),
            },
            additional_location_info=AdditionalLocationInfo(
                central_mid="8024999222",
                central_legal_name="Elavon",
                central_tax_id="787421357",
            ),
            signed_date=DateComponents(
                year=1970,
                month="JAN",
                day=15,
            ),
            signed_type="WET",
            intermediary_owner_info=IntermediaryOwnerInfo(
                intermediary_owners=[
                    IntermediaryOwner(
                        ownership_pct="90",
                        business_name="ACME",
                        owner_name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        phone=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        email_address="email_address_example",
                        address=Address(
                            street_name="Baker Street",
                            street_number="221",
                            line_two="Apt B",
                            line_three="48",
                            city="Atlanta",
                            county="Fulton",
                            post_code="30346",
                            country="USA",
                            state="USA_AL",
                            classification="BUSINESS_STREET_ADDRESS",
                            contact_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            location_name="Baker Plaza",
                        ),
                    ),
                ],
                additional_intermediate_owners=True,
            ),
            revenue_share_info=RevenueShareInfo(
                secondary_sales_person="12345",
                split_percentage="50",
            ),
            elavon_contract="UK",
            internal_use_info=InternalUseInfo(
                field_auto_info=FieldAutoInfo(
                    requested=True,
                    applied=True,
                    monitored=True,
                    values_modified=True,
                    field_auto_reference_id="field_auto_reference_id_example",
                ),
                sales_rep_info=SalesRepInfo(
                    sales_rep_code="12345",
                    name="name_example",
                    email="repname@email.com",
                    submitted=True,
                ),
                tin_applied_to_all=True,
                ip_address="ip_address_example",
            ),
            eframe_info=EframeInfo(
                scheme_selection="scheme_selection_example",
                pos_contract=True,
                is_girocard=True,
            ),
            partner_info=PartnerInfo(
                partner_name="partner_name_example",
                associate_id="associate_id_example",
                book_of_business="book_of_business_example",
                correlation_id="correlation_id_example",
                partner_source="partner_source_example",
                merchant_user_id="merchant_user_id_example",
                session_id="session_id_example",
            ),
            alternative_payment_methods=[
                ApmAcquirer(
                    acquirer_code="acquirer_code_example",
                    acquirer_types=[
                        ApmAcquirerType(
                            type_code="type_code_example",
                            per_item_amount="per_item_amount_example",
                            rate_percentage="rate_percentage_example",
                            pricing_tiers=[
                                ApmPricingTier(
                                    combining_code="combining_code_example",
                                    per_item_amount="per_item_amount_example",
                                    rate_percentage="rate_percentage_example",
                                    description="description_example",
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        profile_code="TEST",
        document_packet_id="42f441d0-0c23-468d-8319-f1e2af17dc15",
    ) # BoardingRequestParams | 

    # example passing only required values which don't have defaults set
    try:
        # Boarding
        api_response = api_instance.board(version_number, body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->board: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_number** | **int**|  |
 **body** | [**BoardingRequestParams**](BoardingRequestParams.md)|  |

### Return type

[**BoardingResponse**](BoardingResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Boarding Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **board_status**
> BoardingStatusResponse board_status(version_number, body)

Boarding Status

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.boarding_status_request_params import BoardingStatusRequestParams
from elavon.model.boarding_status_response import BoardingStatusResponse
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    version_number = 1 # int | 
    body = BoardingStatusRequestParams(
        boarding_id="2101491576",
        correlation_id="correlation_id_example",
        client_id="IDNA",
        unique_id="AcmeCorp1572566399123",
        country="USA",
        sales_rep_code="sales_rep_code_example",
    ) # BoardingStatusRequestParams | 

    # example passing only required values which don't have defaults set
    try:
        # Boarding Status
        api_response = api_instance.board_status(version_number, body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->board_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_number** | **int**|  |
 **body** | [**BoardingStatusRequestParams**](BoardingStatusRequestParams.md)|  |

### Return type

[**BoardingStatusResponse**](BoardingStatusResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Boarding Status Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **board_status_xsd_schema**
> board_status_xsd_schema(version_number)

Get Boarding Status Schema

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    version_number = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get Boarding Status Schema
        api_instance.board_status_xsd_schema(version_number)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->board_status_xsd_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_number** | **int**|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **board_xsd_schema**
> board_xsd_schema(version_number, iso3_country)

Get Boarding Schema

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    version_number = 1 # int | 
    iso3_country = "iso3Country_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Boarding Schema
        api_instance.board_xsd_schema(version_number, iso3_country)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->board_xsd_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_number** | **int**|  |
 **iso3_country** | **str**|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_document_signing_status**
> CheckDocumentSigningStatusResponse check_document_signing_status(body)

Check the signing status of one or more signer of a packet

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.check_document_signing_status_response import CheckDocumentSigningStatusResponse
from elavon.model.check_document_signing_status_request import CheckDocumentSigningStatusRequest
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = CheckDocumentSigningStatusRequest(
        document_packet_id="42f441d0-0c23-468d-8319-f1e2af17dc15",
    ) # CheckDocumentSigningStatusRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Check the signing status of one or more signer of a packet
        api_response = api_instance.check_document_signing_status(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->check_document_signing_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CheckDocumentSigningStatusRequest**](CheckDocumentSigningStatusRequest.md)|  |

### Return type

[**CheckDocumentSigningStatusResponse**](CheckDocumentSigningStatusResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Check Document Signing Status Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document_packet**
> CreateDocumentPacketResponse create_document_packet(body)

Create a document packet

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.create_document_packet_response import CreateDocumentPacketResponse
from elavon.model.create_document_packet_request import CreateDocumentPacketRequest
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = CreateDocumentPacketRequest(
        profile_code="TEST",
        signers=[
            Signer(
                signer_id="signer_id_example",
                signer=Name(
                    salutation="MR",
                    first_name="John",
                    middle_name="Lee",
                    last_name="Doe",
                ),
                email_address="email_address_example",
                principal=True,
                signing_complete_url="signing_complete_url_example",
                signing_decline_url="signing_decline_url_example",
                signing_expired_url="signing_expired_url_example",
                language="language_example",
                opt_in_out1=True,
                opt_in_out2=True,
                opt_in_out3=True,
            ),
        ],
        document_packet_data=DocumentPacketData(
            scarecrow_application=ScarecrowApplication(
                client_id="IDNA",
                client_group_number="860",
                unique_id="AcmeCorp1572566399123",
                banker_id="123",
                banker_partner_id="123",
                country="USA",
                principal=Person(
                    name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    contact_info=ContactInfo(
                        address=Address(
                            street_name="Baker Street",
                            street_number="221",
                            line_two="Apt B",
                            line_three="48",
                            city="Atlanta",
                            county="Fulton",
                            post_code="30346",
                            country="USA",
                            state="USA_AL",
                            classification="BUSINESS_STREET_ADDRESS",
                            contact_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            location_name="Baker Plaza",
                        ),
                        additional_addresses={
                            "key": Address(
                                street_name="Baker Street",
                                street_number="221",
                                line_two="Apt B",
                                line_three="48",
                                city="Atlanta",
                                county="Fulton",
                                post_code="30346",
                                country="USA",
                                state="USA_AL",
                                classification="BUSINESS_STREET_ADDRESS",
                                contact_name=Name(
                                    salutation="MR",
                                    first_name="John",
                                    middle_name="Lee",
                                    last_name="Doe",
                                ),
                                location_name="Baker Plaza",
                            ),
                        },
                        phone=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        mobile=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        fax=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        email_address="contactname@email.com",
                    ),
                    dob=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    positions={
                        "key": True,
                    },
                    ownership_pct="90",
                    ids=[
                        Identification(
                            id_type="PASSPORT",
                            id_number="123456789",
                            expiry_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issue_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issuing_country="USA",
                            issuing_state="USA_AL",
                            id_name="id_name_example",
                            issuing_agency="issuing_agency_example",
                        ),
                    ],
                    title_type="ACCOUNTING_MANAGER",
                    title="Chief Technology Officer",
                    signing_personal_guarantee=True,
                    responsible_party=True,
                    related_party=True,
                    residing_country="GBR",
                    primary_nationality="GBR",
                    secondary_nationality="IRL",
                    documentary_info=DocumentaryInfo(
                        documentary=True,
                        documentary_verifier="SALES_TEAM",
                        documentary_issuer="USA",
                        documentary_type="DRIVER_LICENSE",
                        id_number="111111117",
                        issue_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        expiry_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        issuing_state="USA_AL",
                        foreign_issuing_state="foreign_issuing_state_example",
                    ),
                    alternate_address_info=AlternateAddressInfo(
                        document_needed=True,
                        document_verified=True,
                        alternate_address_document_type="BANK_STATEMENT",
                        document_name="document_name_example",
                    ),
                    is_new_owner=True,
                    directional_ownership_type="DIRECT_OWNERSHIP",
                    signing_agreement=True,
                    us_person=True,
                ),
                business_info=BusinessInfo(
                    dba_name="Grimm's Bookstore",
                    dba_name_extended="Grimm's Fairytales and Other Stories Bookstore",
                    business_address=Address(
                        street_name="Baker Street",
                        street_number="221",
                        line_two="Apt B",
                        line_three="48",
                        city="Atlanta",
                        county="Fulton",
                        post_code="30346",
                        country="USA",
                        state="USA_AL",
                        classification="BUSINESS_STREET_ADDRESS",
                        contact_name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        location_name="Baker Plaza",
                    ),
                    legal_name="Barkers Dog Bakery",
                    legal_name_extended="Baking Better Biscuits for Your Favorite Barkers Dog Bakery LLC",
                    legal_name_marked=[
                        "legal_name_marked_example",
                    ],
                    additional_addresses={
                        "key": Address(
                            street_name="Baker Street",
                            street_number="221",
                            line_two="Apt B",
                            line_three="48",
                            city="Atlanta",
                            county="Fulton",
                            post_code="30346",
                            country="USA",
                            state="USA_AL",
                            classification="BUSINESS_STREET_ADDRESS",
                            contact_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            location_name="Baker Plaza",
                        ),
                    },
                    ownership_type="SOLE_TRADER",
                    registration_number="1234567",
                    tax_id="787421357",
                    tax_id_type="FEDERAL_TAX_ID",
                    vat_info=VatInfo(
                        number_option="VAT_NBR",
                        number56_b="123456789",
                        expiry_date56_b=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        tax_number_type="CORPORATE_TAX_NUMBER",
                        tax_number="tax_number_example",
                    ),
                    tax_form_type="W9",
                    tax_class_type="CORPORATION",
                    customer_membership_number="111222",
                    product_description="Bakeries",
                    mcc_code="7399E",
                    establishment_year="2005",
                    current_ownership_years="3",
                    current_ownership_months="6",
                    government_owned_entity=True,
                    communication_language="en",
                    pos_language="en",
                    store_number="123456789",
                    association_codes=[
                        "12345",
                    ],
                    opt_out=True,
                    sign_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    pci_info=PCIInfo(
                        pci_program_level="ONE",
                        pci_service_type="BASIC",
                        pci_contact_first_name="pci_contact_first_name_example",
                        pci_contact_last_name="pci_contact_last_name_example",
                        pci_contact_email_address="pci_contact_email_address_example",
                        pci_contact_phone=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        pci_groups=[
                            "PCI_PROGRAM_EXCLUSION",
                        ],
                    ),
                    employer_id="1234567",
                    country_of_origin="USA",
                    exemption_type="ADDITIONAL_LOCATION",
                    owner_exemption_type="BANK_ADVISED_POOLED",
                    number_of_partners="ONE",
                    relationship_mgr_code="1234567",
                    country_of_primary_operation="USA",
                    bearer_shares=True,
                    legal_status="CERTIFIED_INCORPORATION_ARTICLES",
                    verifications={
                        "key": VerificationInfo(
                            documentary=True,
                            issuing_country="USA",
                            issuing_state="USA_AL",
                            site_person_met="John Smith",
                            site_visit_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            id_number="111111117",
                            issue_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            expiry_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            document_type="CERTIFIED_INCORPORATION_ARTICLES",
                        ),
                    },
                    industry_class="LODGING",
                    no_plates=True,
                    agent_number="1223334",
                    location_mid_range="NORDIC",
                    hemp_grower_info=HempGrowerInfo(
                        operations_description="operations_description_example",
                        is_licensed=True,
                        license_expiration_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        additional_mrb_activity=True,
                        cannabis_revenue_percentage_range="NONE",
                    ),
                    credit_decision_info=CreditDecisionInfo(
                        credit_decision_flag=True,
                        credit_decision_id="credit_decision_id_example",
                    ),
                ),
                financial_info=FinancialInfo(
                    avg_sale_amount="125",
                    monthly_card_sales="1000",
                    annual_card_sales="12000",
                    annual_revenue="240000",
                    highest_ticket_amount="1000",
                    highest_ticket_frequency=1,
                    funding_currency="USD",
                    card_present_acceptance_percent="100",
                    internet_acceptance_percent="0",
                    moto_acceptance_percent="0",
                    business_email_address="business_email_address_example",
                    business_website_url="business@email.com",
                    customer_service_phone=PhoneNumber(
                        intl_code="44",
                        area_code="111",
                        number="1231234",
                        extension="2",
                    ),
                    not_present_delay_days=0,
                    deposit_frequency="0",
                    deposit_size_percent="1",
                    deposit_balance_days="1",
                    deposit_fulfillment_days="1",
                    full_payment_percent="1",
                    full_payment_fulfillment="1",
                    utilize_cvv2=True,
                    recurring_transactions=True,
                    contract_term_type="ZERO_MONTH",
                    months_closed=[
                        "JAN",
                    ],
                    monetary_billing_method="CARD_DISCOUNT",
                    authorization_included=True,
                    annual_fee_month_start="JAN",
                    money_services=True,
                    payment_services=True,
                    third_party_processor=True,
                    non_government_non_profit=True,
                    daily_discount=True,
                    non_bank_atm=True,
                    embassy=True,
                    high_inter_annual_trans_ngo=True,
                ),
                sales_rep_code="12345",
                additional_shareholders=[
                    Person(
                        name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        contact_info=ContactInfo(
                            address=Address(
                                street_name="Baker Street",
                                street_number="221",
                                line_two="Apt B",
                                line_three="48",
                                city="Atlanta",
                                county="Fulton",
                                post_code="30346",
                                country="USA",
                                state="USA_AL",
                                classification="BUSINESS_STREET_ADDRESS",
                                contact_name=Name(
                                    salutation="MR",
                                    first_name="John",
                                    middle_name="Lee",
                                    last_name="Doe",
                                ),
                                location_name="Baker Plaza",
                            ),
                            additional_addresses={
                                "key": Address(
                                    street_name="Baker Street",
                                    street_number="221",
                                    line_two="Apt B",
                                    line_three="48",
                                    city="Atlanta",
                                    county="Fulton",
                                    post_code="30346",
                                    country="USA",
                                    state="USA_AL",
                                    classification="BUSINESS_STREET_ADDRESS",
                                    contact_name=Name(
                                        salutation="MR",
                                        first_name="John",
                                        middle_name="Lee",
                                        last_name="Doe",
                                    ),
                                    location_name="Baker Plaza",
                                ),
                            },
                            phone=PhoneNumber(
                                intl_code="44",
                                area_code="111",
                                number="1231234",
                                extension="2",
                            ),
                            mobile=PhoneNumber(
                                intl_code="44",
                                area_code="111",
                                number="1231234",
                                extension="2",
                            ),
                            fax=PhoneNumber(
                                intl_code="44",
                                area_code="111",
                                number="1231234",
                                extension="2",
                            ),
                            email_address="contactname@email.com",
                        ),
                        dob=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        positions={
                            "key": True,
                        },
                        ownership_pct="90",
                        ids=[
                            Identification(
                                id_type="PASSPORT",
                                id_number="123456789",
                                expiry_date=DateComponents(
                                    year=1970,
                                    month="JAN",
                                    day=15,
                                ),
                                issue_date=DateComponents(
                                    year=1970,
                                    month="JAN",
                                    day=15,
                                ),
                                issuing_country="USA",
                                issuing_state="USA_AL",
                                id_name="id_name_example",
                                issuing_agency="issuing_agency_example",
                            ),
                        ],
                        title_type="ACCOUNTING_MANAGER",
                        title="Chief Technology Officer",
                        signing_personal_guarantee=True,
                        responsible_party=True,
                        related_party=True,
                        residing_country="GBR",
                        primary_nationality="GBR",
                        secondary_nationality="IRL",
                        documentary_info=DocumentaryInfo(
                            documentary=True,
                            documentary_verifier="SALES_TEAM",
                            documentary_issuer="USA",
                            documentary_type="DRIVER_LICENSE",
                            id_number="111111117",
                            issue_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            expiry_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issuing_state="USA_AL",
                            foreign_issuing_state="foreign_issuing_state_example",
                        ),
                        alternate_address_info=AlternateAddressInfo(
                            document_needed=True,
                            document_verified=True,
                            alternate_address_document_type="BANK_STATEMENT",
                            document_name="document_name_example",
                        ),
                        is_new_owner=True,
                        directional_ownership_type="DIRECT_OWNERSHIP",
                        signing_agreement=True,
                        us_person=True,
                    ),
                ],
                contact=Person(
                    name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    contact_info=ContactInfo(
                        address=Address(
                            street_name="Baker Street",
                            street_number="221",
                            line_two="Apt B",
                            line_three="48",
                            city="Atlanta",
                            county="Fulton",
                            post_code="30346",
                            country="USA",
                            state="USA_AL",
                            classification="BUSINESS_STREET_ADDRESS",
                            contact_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            location_name="Baker Plaza",
                        ),
                        additional_addresses={
                            "key": Address(
                                street_name="Baker Street",
                                street_number="221",
                                line_two="Apt B",
                                line_three="48",
                                city="Atlanta",
                                county="Fulton",
                                post_code="30346",
                                country="USA",
                                state="USA_AL",
                                classification="BUSINESS_STREET_ADDRESS",
                                contact_name=Name(
                                    salutation="MR",
                                    first_name="John",
                                    middle_name="Lee",
                                    last_name="Doe",
                                ),
                                location_name="Baker Plaza",
                            ),
                        },
                        phone=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        mobile=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        fax=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        email_address="contactname@email.com",
                    ),
                    dob=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    positions={
                        "key": True,
                    },
                    ownership_pct="90",
                    ids=[
                        Identification(
                            id_type="PASSPORT",
                            id_number="123456789",
                            expiry_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issue_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issuing_country="USA",
                            issuing_state="USA_AL",
                            id_name="id_name_example",
                            issuing_agency="issuing_agency_example",
                        ),
                    ],
                    title_type="ACCOUNTING_MANAGER",
                    title="Chief Technology Officer",
                    signing_personal_guarantee=True,
                    responsible_party=True,
                    related_party=True,
                    residing_country="GBR",
                    primary_nationality="GBR",
                    secondary_nationality="IRL",
                    documentary_info=DocumentaryInfo(
                        documentary=True,
                        documentary_verifier="SALES_TEAM",
                        documentary_issuer="USA",
                        documentary_type="DRIVER_LICENSE",
                        id_number="111111117",
                        issue_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        expiry_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        issuing_state="USA_AL",
                        foreign_issuing_state="foreign_issuing_state_example",
                    ),
                    alternate_address_info=AlternateAddressInfo(
                        document_needed=True,
                        document_verified=True,
                        alternate_address_document_type="BANK_STATEMENT",
                        document_name="document_name_example",
                    ),
                    is_new_owner=True,
                    directional_ownership_type="DIRECT_OWNERSHIP",
                    signing_agreement=True,
                    us_person=True,
                ),
                bank_accounts={
                    "key": BankingInfo(
                        account_name="John Doe",
                        bank_name="Wells Fargo",
                        urgent_payment=True,
                        funding_method="NETCREDIT",
                        account_number="20581687",
                        sort_code="121000248",
                        iban="GB48LOYD3037341",
                        swift_code="CPRTGB22",
                        bank_creditor_id="bank_creditor_id_example",
                        bank_direct=True,
                        country="GBR",
                        tape_id="14",
                        true_daily=True,
                        use_chain_account_number=True,
                    ),
                },
                card_pricing=CardPricing(
                    pricing_method="CLEAR_AND_SIMPLE",
                    pricing_category="RETAIL",
                    amex_accepting_info=AmexAcceptingInfo(
                        amex_monthly_card_sales=3553.0,
                        is_existing=True,
                        amex_mid="2101491576",
                    ),
                    payment_facilitator_info=PaymentFacilitatorInfo(
                        payment_facilitator_type="PAYMENT_FACILITATOR",
                        card_prefixes=[
                            CardPrefix(
                                card_type="VISA",
                                prefix="DE",
                            ),
                        ],
                    ),
                    card_charges=[
                        CardCharge(
                            card_type="VISA",
                            minimum_fee=0.03,
                            authorization_fee=3.14,
                            se_number="123456789",
                            service_type="PARTIAL_SERVICE",
                            card_funding="ELAVON",
                            pricing_tiers={
                                "key": PricingTier(
                                    discount_rate=2.0,
                                    discount_per_item=0.2,
                                ),
                            },
                        ),
                    ],
                    exception_charges=[
                        ExceptionCharge(
                            type="BUSINESS_CARDS",
                            discount_rate=1.0,
                            discount_per_item=0.1,
                        ),
                    ],
                    debit_pricing=DebitPricing(
                        pricing_method="INTERCHANGE_DIFFERENTIAL",
                        authorization_method="FIXED",
                        surcharge_amount=1.1,
                        surcharge_percent="0.1",
                        debit_network_charges=[
                            DebitNetworkCharge(
                                type="INTERLINK",
                                discount_rate=5.0,
                                discount_per_item=0.5,
                                per_auth=3.14,
                            ),
                        ],
                        pinless_setup=True,
                    ),
                ),
                fees=[
                    Fee(
                        type="JOI",
                        quantity=1,
                        amount=9.99,
                        frequency="ANNUAL",
                        start_month="JAN",
                    ),
                ],
                monetary_pricing_program="monetary_pricing_program_example",
                authenticate_pricing_program="47777",
                parent_entity="parent_entity_example",
                short_name="MS00EPNA",
                fraud_check_result=FraudCheckResult(
                    transaction_id="1100000000540130",
                    decision="PASS",
                ),
                site_survey=SiteSurvey(
                    site_survey_conducted=True,
                    location_type="SHOPPING_CENTRE",
                    site_address_same_as_dba=True,
                    location_environment="BUSINESS_DISTRICT",
                    vicinity_condition="WELL_KEPT",
                    location_square_meters="LTE_TO_250",
                    location_appearance="VERY_GOOD",
                    business_operating=True,
                    inventory_display_adequate=True,
                    inventory_consistent_with_business_type=True,
                    card_decals_visible=True,
                    card_decals_installed_at_visit=True,
                ),
                dynamic_currency_conversion=DynamicCurrencyConversion(
                    rebate_percent=0.5,
                    mark_up="ZERO",
                    currency_group="FIVE_USD_DCC_CURRENCIES",
                    registration_fee=2.0,
                ),
                billing_statement=BillingStatement(
                    type="SURCHARGE_TIERED",
                    media="DYNAMIC_MERCHANT_REPORTING",
                    address_type="BUSINESS",
                    email_address="applicantname@email.com",
                    frequency="DAILY",
                ),
                funding_statement=FundingStatement(
                    type="SURCHARGE_TIERED",
                    media="DYNAMIC_MERCHANT_REPORTING",
                    email_address="applicant@email.com",
                    frequency="DAILY",
                ),
                electronic_statement=ElectronicStatement(
                    type="SURCHARGE_TIERED",
                    media="DYNAMIC_MERCHANT_REPORTING",
                    email_address="applicant@email.com",
                    frequency="DAILY",
                ),
                vat_invoice_statement=VatInvoiceStatement(
                    type="SURCHARGE_TIERED",
                    media="DYNAMIC_MERCHANT_REPORTING",
                    address_type="BUSINESS",
                ),
                billing_method="NETCREDIT",
                referrer_name="PARTNER_BANK",
                referrer_reference_number="11",
                previous_processor="previous_processor_example",
                value_added_info=ValueAddedInfo(
                    value_adds={
                        "key": True,
                    },
                    ebt_info=EbtInfo(
                        se_number="123456789",
                        authorization_fee=0.03,
                    ),
                    ecs_info=EcsInfo(
                        processing_acceptance_type="POP_POS_IMAGE",
                        service_level_type="GUARANTEE_WITH_VERIFY",
                        annual_check_volume=100000.0,
                        average_check_amount=25.0,
                        max_check_amount=1000,
                        per_transaction=0.0,
                        discount_rate=0.0,
                        monthly_minimum=0.0,
                        per_return_fee=0.0,
                        nsf_service_processing_fee=0.0,
                        nsf_service_fee=0.0,
                        collection=True,
                        enquire_reporting=True,
                        service_provider_type="ENCIRCLE_DIRECT",
                    ),
                    acs_info=AcsInfo(
                        reporting_id="reporting_id_example",
                    ),
                    fanfare_info=FanfareInfo(
                        max_card_value="max_card_value_example",
                        package_type="STANDARD_GIFT_LOYALTY",
                        enrollment={
                            "key": EnrollmentInfo(
                                discount_rate=0.0,
                                discount_amount=0.0,
                            ),
                        },
                        loyalty={
                            "key": LoyaltyInfo(
                                visits=1,
                                amount_spent=22.0,
                                discount_rate=1.1,
                                discount_amount=5.0,
                            ),
                        },
                    ),
                    gsm_prepaid_type="EURONET_NO_PAYS",
                    surcharge_managed_by="surcharge_managed_by_example",
                    credit_surcharge_amt="credit_surcharge_amt_example",
                    efs3d_secure_info=Efs3dSecureInfo(
                        billing_per_item_fee=3.14,
                    ),
                    straight_send_info=StraightSendInfo(
                        per_transaction_fee=3.14,
                        percent_fee=3.14,
                    ),
                    on_demand_info=OnDemandInfo(
                        per_transaction_fee=3.14,
                        percent_fee=3.14,
                    ),
                    ocm_info=OcmInfo(
                        setup_type="Mid, Chain",
                        setup_fee=0.0,
                        monthly_fee=0.0,
                        number_of_users=1,
                    ),
                ),
                equipment_info=EquipmentInfo(
                    equipment_items=[
                        EquipmentItem(
                            code="310T3",
                            quantity=2,
                            pricing_items=[
                                EquipmentPricing(
                                    amount=200.0,
                                    purchase_type="EXCHANGE",
                                    lease_term=1,
                                    vendor_code=1,
                                    vendor_plan="vendor_plan_example",
                                    start_month="JAN",
                                    start_year="2010",
                                ),
                            ],
                            item_settings=ItemSettings(
                                security_level="BASIC",
                                semi_integrated=True,
                                connection_type="STANDARD_IP",
                                close_method="MANUAL",
                                capture_method="HOST",
                                qir_vendor="qir_vendor_example",
                                services={
                                    "key": True,
                                },
                                options=[
                                    EquipmentOption(
                                        integrator_code="integrator_code_example",
                                        ciers_number="ciers_number_example",
                                        serial_number="serial_number_example",
                                        model_number="model_number_example",
                                        ecr_type="SMARTLINK",
                                        ecr_mode="LITE_TOUCH",
                                        print_via_ecr=True,
                                        ecr_integrator="ALMAR",
                                        ecr_cable_type="NONE",
                                        epg_integration_type="REMOTE",
                                        bax_number="bax_number_example",
                                        bax_effective_date=DateComponents(
                                            year=1970,
                                            month="JAN",
                                            day=15,
                                        ),
                                    ),
                                ],
                                bundled_thresh_hold=1,
                                service_pricing_code="CORE",
                                terminal_type="INTERNET",
                                ingenico_pay_table=True,
                                deploy_type="DEPLOY",
                            ),
                            exception_items=[
                                ExceptionItem(
                                    type="type_example",
                                    discount_rate=3.14,
                                    discount_per_item=3.14,
                                ),
                            ],
                            service_fee=3.14,
                            trx_free_month=1,
                            future_effective_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                        ),
                    ],
                    terminal_services=[
                        TerminalService(
                            type="QUICK_CLOSE",
                            service_specifics="service_specifics_example",
                        ),
                    ],
                    training_type="TRAINING",
                    shipping_method="NEXT_DAY",
                    network="ELAVON",
                    fusebox_info=FuseboxInfo(
                        simplify_quantity=1,
                        direct_quantity=1,
                        simplify_location="simplify_location_example",
                        direct_to_fusebox_location="direct_to_fusebox_location_example",
                    ),
                    anticipated_start_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                ),
                branch_number="111",
                branch_code="1234",
                self_boarded_external=True,
                employee_number="11222",
                rep_referral_number="321",
                promotional_code="00001",
                chain_info=ChainInfo(
                    chain_number="chain_number_example",
                    chain_name="chain_name_example",
                    send_statement_to_address="BUSINESS",
                    statement_media="DYNAMIC_MERCHANT_REPORTING",
                    address=Address(
                        street_name="Baker Street",
                        street_number="221",
                        line_two="Apt B",
                        line_three="48",
                        city="Atlanta",
                        county="Fulton",
                        post_code="30346",
                        country="USA",
                        state="USA_AL",
                        classification="BUSINESS_STREET_ADDRESS",
                        contact_name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        location_name="Baker Plaza",
                    ),
                    chain_level_billing=True,
                    bank_accounts={
                        "key": BankingInfo(
                            account_name="John Doe",
                            bank_name="Wells Fargo",
                            urgent_payment=True,
                            funding_method="NETCREDIT",
                            account_number="20581687",
                            sort_code="121000248",
                            iban="GB48LOYD3037341",
                            swift_code="CPRTGB22",
                            bank_creditor_id="bank_creditor_id_example",
                            bank_direct=True,
                            country="GBR",
                            tape_id="14",
                            true_daily=True,
                            use_chain_account_number=True,
                        ),
                    },
                ),
                distributions={
                    "key": DistributionInfo(
                        method="MAILING",
                        address_type="BUSINESS",
                        email_address="applicant@email.com",
                    ),
                },
                additional_location_info=AdditionalLocationInfo(
                    central_mid="8024999222",
                    central_legal_name="Elavon",
                    central_tax_id="787421357",
                ),
                signed_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                signed_type="WET",
                intermediary_owner_info=IntermediaryOwnerInfo(
                    intermediary_owners=[
                        IntermediaryOwner(
                            ownership_pct="90",
                            business_name="ACME",
                            owner_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            phone=PhoneNumber(
                                intl_code="44",
                                area_code="111",
                                number="1231234",
                                extension="2",
                            ),
                            email_address="email_address_example",
                            address=Address(
                                street_name="Baker Street",
                                street_number="221",
                                line_two="Apt B",
                                line_three="48",
                                city="Atlanta",
                                county="Fulton",
                                post_code="30346",
                                country="USA",
                                state="USA_AL",
                                classification="BUSINESS_STREET_ADDRESS",
                                contact_name=Name(
                                    salutation="MR",
                                    first_name="John",
                                    middle_name="Lee",
                                    last_name="Doe",
                                ),
                                location_name="Baker Plaza",
                            ),
                        ),
                    ],
                    additional_intermediate_owners=True,
                ),
                revenue_share_info=RevenueShareInfo(
                    secondary_sales_person="12345",
                    split_percentage="50",
                ),
                elavon_contract="UK",
                internal_use_info=InternalUseInfo(
                    field_auto_info=FieldAutoInfo(
                        requested=True,
                        applied=True,
                        monitored=True,
                        values_modified=True,
                        field_auto_reference_id="field_auto_reference_id_example",
                    ),
                    sales_rep_info=SalesRepInfo(
                        sales_rep_code="12345",
                        name="name_example",
                        email="repname@email.com",
                        submitted=True,
                    ),
                    tin_applied_to_all=True,
                    ip_address="ip_address_example",
                ),
                eframe_info=EframeInfo(
                    scheme_selection="scheme_selection_example",
                    pos_contract=True,
                    is_girocard=True,
                ),
                partner_info=PartnerInfo(
                    partner_name="partner_name_example",
                    associate_id="associate_id_example",
                    book_of_business="book_of_business_example",
                    correlation_id="correlation_id_example",
                    partner_source="partner_source_example",
                    merchant_user_id="merchant_user_id_example",
                    session_id="session_id_example",
                ),
                alternative_payment_methods=[
                    ApmAcquirer(
                        acquirer_code="acquirer_code_example",
                        acquirer_types=[
                            ApmAcquirerType(
                                type_code="type_code_example",
                                per_item_amount="per_item_amount_example",
                                rate_percentage="rate_percentage_example",
                                pricing_tiers=[
                                    ApmPricingTier(
                                        combining_code="combining_code_example",
                                        per_item_amount="per_item_amount_example",
                                        rate_percentage="rate_percentage_example",
                                        description="description_example",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            language="language_example",
            agreement_id="agreement_id_example",
            is_grouped_application=True,
            wet_signed=True,
            card_volume=CardVolume(
                visa_percentage="15.6",
                master_card_percentage="12.3",
                amex_percentage="4.5",
                amex_average_transaction="10.1",
                interac_average_transaction="23.4",
            ),
            vendor_info=ProviderInfo(
                representative_name="Alex Smith",
                representative_email="asmith@email.com",
                representative_sales_code="12345",
                representative_contact_number=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
            ),
            acting_intermediary_info=ActingIntermediaryInfo(
                acting_intermediary_name="acting_intermediary_name_example",
                acting_intermediary_type="QUALIFIED_INTERMEDIARY",
            ),
            bank_account_details_map={
                "key": BankAccountAdditionalInfo(
                    bank_name="bank_name_example",
                    bank_branch="bank_branch_example",
                    direct_debit_authorized=True,
                ),
            },
            is_tax_exempt_equipment=True,
            talech_egift_only=True,
            displayed_currency="displayed_currency_example",
            additional_description_info=AdditionalDescriptionInfo(
                previous_processor_description="Bank of America",
                monetary_pricing_program_description="MIF Unblended",
                referrer_reference_description="referrer_reference_description_example",
                notes="notes_example",
            ),
            additional_value_added_service_info=ValueAddedServices(
                ecs=ElectronicCheckService(
                    reporting_fee=3.14,
                    reporting_num_users="reporting_num_users_example",
                    ach_check_questions=AchCheckQuestions(
                        payment_acceptance_type="payment_acceptance_type_example",
                        prior_acceptance_authorization=True,
                        customer_identification=True,
                        ach_customer_type="EXISTING",
                        maintain_and_disclose_cancel=True,
                        ensure_accurate_transaction_info=True,
                    ),
                ),
                fanfare=Fanfare(
                    setup_fee=1.1,
                    monthly_fee=0.06,
                    annual_fee=1.6,
                    custom_card_upgrade_fee=0.02,
                    included_cards=FanfareCardSplits(
                        promotional="promotional_example",
                        loyalty="loyalty_example",
                        gift="gift_example",
                    ),
                    additional_cards_type="FF_STANDARD",
                    additional_cards=FanfareCardSplits(
                        promotional="promotional_example",
                        loyalty="loyalty_example",
                        gift="gift_example",
                    ),
                    additional_card_price=3.14,
                    program_checkup=3.14,
                    card_style="card_style_example",
                    justification_type="LEFT",
                    card_is_text=True,
                    card_text="card_text_example",
                    text_case_type="TITLE_CASE",
                    text_color="text_color_example",
                    text_font="text_font_example",
                ),
            ),
            additional_business_info=AdditionalBusinessInfo(
                ownership_years_over_range="3",
                is_max_establishment_year=True,
                has_government_incentive=True,
            ),
            funding_type="STANDARD",
            integrator_solution_info=IntegratorSolutionInfo(
                health_care_eligibility_selection_map={
                    "key": HealthCareEligibilityInfo(
                        monthly_fee=0.0,
                        npi_numbers=[
                            "npi_numbers_example",
                        ],
                    ),
                },
                payments=Payments(
                    pms_vendor_pas="pms_vendor_pas_example",
                    number_of_providers="1",
                    sales_rep_phone_number="sales_rep_phone_number_example",
                    integrator_notes="1111111111",
                    has_payment_plans=True,
                ),
                has_ecs_only=True,
                sku="310T3",
            ),
            additional_lease_info=AdditionalLeaseInfo(
                lease_details_map={
                    "key": LeaseDetails(
                        alternate_price=3.14,
                        pricing_plan="pricing_plan_example",
                    ),
                },
            ),
            marketing_data_consent_map={
                "key": True,
            },
            additional_site_survey_info=AdditionalSiteSurveyInfo(
                incomplete_survey_reason_type="NOT_OPEN",
                site_survey_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                site_survey_conducted_by="site_survey_conducted_by_example",
                description_of_no_site_survey="description_of_no_site_survey_example",
            ),
            kyc_quiz_status_map={
                "KYC_RESULT_FAILED_QUIZ": "KYC_RESULT_FAILED_QUIZ",
            },
            var_other_details=VarOtherDetails(
                var_type="VENDOR_DISTRIBUTED",
                vendor="vendor_example",
                product="product_example",
                version="version_example",
            ),
            additional_card_pricing_info=AdditionalCardPricingInfo(
                minimum_card_fee=0.0,
                clear_and_simple_type="clear_and_simple_type_example",
                c4_pricing_type="c4_pricing_type_example",
                high_risk_cost_additional_loading="high_risk_cost_additional_loading_example",
            ),
            sales_office_contact=SalesOfficeContact(
                address=Address(
                    street_name="Baker Street",
                    street_number="221",
                    line_two="Apt B",
                    line_three="48",
                    city="Atlanta",
                    county="Fulton",
                    post_code="30346",
                    country="USA",
                    state="USA_AL",
                    classification="BUSINESS_STREET_ADDRESS",
                    contact_name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    location_name="Baker Plaza",
                ),
                phone=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
            ),
            sales_person_contact=SalesPersonContact(
                name=Name(
                    salutation="MR",
                    first_name="John",
                    middle_name="Lee",
                    last_name="Doe",
                ),
                phone=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                email_address="email_address_example",
            ),
            additional_auth_pricing_program_info=AdditionalAuthPricingProgramInfo(
                description="description_example",
                fee=5.0,
                auth_amount=10.0,
            ),
            applicant_email="applicant_email_example",
            partner_document_data={
                "key": {
                    "key": "key_example",
                },
            },
            application_id=1,
        ),
    ) # CreateDocumentPacketRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a document packet
        api_response = api_instance.create_document_packet(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->create_document_packet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDocumentPacketRequest**](CreateDocumentPacketRequest.md)|  |

### Return type

[**CreateDocumentPacketResponse**](CreateDocumentPacketResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Create Document Packet Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_document_packet**
> CreateGroupDocumentPacketResponse create_group_document_packet(body)

Create Group Document Packet

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.create_group_document_packet_response import CreateGroupDocumentPacketResponse
from elavon.model.create_group_document_packet_request import CreateGroupDocumentPacketRequest
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = CreateGroupDocumentPacketRequest(
        channel_code="channel_code_example",
    ) # CreateGroupDocumentPacketRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Group Document Packet
        api_response = api_instance.create_group_document_packet(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->create_group_document_packet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateGroupDocumentPacketRequest**](CreateGroupDocumentPacketRequest.md)|  |

### Return type

[**CreateGroupDocumentPacketResponse**](CreateGroupDocumentPacketResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Create Group Document Packet Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_check**
> CreditCheckResponse credit_check(version_number, body)

Credit Check

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.scarecrow_application import ScarecrowApplication
from elavon.model.credit_check_response import CreditCheckResponse
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    version_number = 1 # int | 
    body = ScarecrowApplication(
        client_id="IDNA",
        client_group_number="860",
        unique_id="AcmeCorp1572566399123",
        banker_id="123",
        banker_partner_id="123",
        country="USA",
        principal=Person(
            name=Name(
                salutation="MR",
                first_name="John",
                middle_name="Lee",
                last_name="Doe",
            ),
            contact_info=ContactInfo(
                address=Address(
                    street_name="Baker Street",
                    street_number="221",
                    line_two="Apt B",
                    line_three="48",
                    city="Atlanta",
                    county="Fulton",
                    post_code="30346",
                    country="USA",
                    state="USA_AL",
                    classification="BUSINESS_STREET_ADDRESS",
                    contact_name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    location_name="Baker Plaza",
                ),
                additional_addresses={
                    "key": Address(
                        street_name="Baker Street",
                        street_number="221",
                        line_two="Apt B",
                        line_three="48",
                        city="Atlanta",
                        county="Fulton",
                        post_code="30346",
                        country="USA",
                        state="USA_AL",
                        classification="BUSINESS_STREET_ADDRESS",
                        contact_name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        location_name="Baker Plaza",
                    ),
                },
                phone=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                mobile=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                fax=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                email_address="contactname@email.com",
            ),
            dob=DateComponents(
                year=1970,
                month="JAN",
                day=15,
            ),
            positions={
                "key": True,
            },
            ownership_pct="90",
            ids=[
                Identification(
                    id_type="PASSPORT",
                    id_number="123456789",
                    expiry_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    issue_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    issuing_country="USA",
                    issuing_state="USA_AL",
                    id_name="id_name_example",
                    issuing_agency="issuing_agency_example",
                ),
            ],
            title_type="ACCOUNTING_MANAGER",
            title="Chief Technology Officer",
            signing_personal_guarantee=True,
            responsible_party=True,
            related_party=True,
            residing_country="GBR",
            primary_nationality="GBR",
            secondary_nationality="IRL",
            documentary_info=DocumentaryInfo(
                documentary=True,
                documentary_verifier="SALES_TEAM",
                documentary_issuer="USA",
                documentary_type="DRIVER_LICENSE",
                id_number="111111117",
                issue_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                expiry_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                issuing_state="USA_AL",
                foreign_issuing_state="foreign_issuing_state_example",
            ),
            alternate_address_info=AlternateAddressInfo(
                document_needed=True,
                document_verified=True,
                alternate_address_document_type="BANK_STATEMENT",
                document_name="document_name_example",
            ),
            is_new_owner=True,
            directional_ownership_type="DIRECT_OWNERSHIP",
            signing_agreement=True,
            us_person=True,
        ),
        business_info=BusinessInfo(
            dba_name="Grimm's Bookstore",
            dba_name_extended="Grimm's Fairytales and Other Stories Bookstore",
            business_address=Address(
                street_name="Baker Street",
                street_number="221",
                line_two="Apt B",
                line_three="48",
                city="Atlanta",
                county="Fulton",
                post_code="30346",
                country="USA",
                state="USA_AL",
                classification="BUSINESS_STREET_ADDRESS",
                contact_name=Name(
                    salutation="MR",
                    first_name="John",
                    middle_name="Lee",
                    last_name="Doe",
                ),
                location_name="Baker Plaza",
            ),
            legal_name="Barkers Dog Bakery",
            legal_name_extended="Baking Better Biscuits for Your Favorite Barkers Dog Bakery LLC",
            legal_name_marked=[
                "legal_name_marked_example",
            ],
            additional_addresses={
                "key": Address(
                    street_name="Baker Street",
                    street_number="221",
                    line_two="Apt B",
                    line_three="48",
                    city="Atlanta",
                    county="Fulton",
                    post_code="30346",
                    country="USA",
                    state="USA_AL",
                    classification="BUSINESS_STREET_ADDRESS",
                    contact_name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    location_name="Baker Plaza",
                ),
            },
            ownership_type="SOLE_TRADER",
            registration_number="1234567",
            tax_id="787421357",
            tax_id_type="FEDERAL_TAX_ID",
            vat_info=VatInfo(
                number_option="VAT_NBR",
                number56_b="123456789",
                expiry_date56_b=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                tax_number_type="CORPORATE_TAX_NUMBER",
                tax_number="tax_number_example",
            ),
            tax_form_type="W9",
            tax_class_type="CORPORATION",
            customer_membership_number="111222",
            product_description="Bakeries",
            mcc_code="7399E",
            establishment_year="2005",
            current_ownership_years="3",
            current_ownership_months="6",
            government_owned_entity=True,
            communication_language="en",
            pos_language="en",
            store_number="123456789",
            association_codes=[
                "12345",
            ],
            opt_out=True,
            sign_date=DateComponents(
                year=1970,
                month="JAN",
                day=15,
            ),
            pci_info=PCIInfo(
                pci_program_level="ONE",
                pci_service_type="BASIC",
                pci_contact_first_name="pci_contact_first_name_example",
                pci_contact_last_name="pci_contact_last_name_example",
                pci_contact_email_address="pci_contact_email_address_example",
                pci_contact_phone=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                pci_groups=[
                    "PCI_PROGRAM_EXCLUSION",
                ],
            ),
            employer_id="1234567",
            country_of_origin="USA",
            exemption_type="ADDITIONAL_LOCATION",
            owner_exemption_type="BANK_ADVISED_POOLED",
            number_of_partners="ONE",
            relationship_mgr_code="1234567",
            country_of_primary_operation="USA",
            bearer_shares=True,
            legal_status="CERTIFIED_INCORPORATION_ARTICLES",
            verifications={
                "key": VerificationInfo(
                    documentary=True,
                    issuing_country="USA",
                    issuing_state="USA_AL",
                    site_person_met="John Smith",
                    site_visit_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    id_number="111111117",
                    issue_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    expiry_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    document_type="CERTIFIED_INCORPORATION_ARTICLES",
                ),
            },
            industry_class="LODGING",
            no_plates=True,
            agent_number="1223334",
            location_mid_range="NORDIC",
            hemp_grower_info=HempGrowerInfo(
                operations_description="operations_description_example",
                is_licensed=True,
                license_expiration_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                additional_mrb_activity=True,
                cannabis_revenue_percentage_range="NONE",
            ),
            credit_decision_info=CreditDecisionInfo(
                credit_decision_flag=True,
                credit_decision_id="credit_decision_id_example",
            ),
        ),
        financial_info=FinancialInfo(
            avg_sale_amount="125",
            monthly_card_sales="1000",
            annual_card_sales="12000",
            annual_revenue="240000",
            highest_ticket_amount="1000",
            highest_ticket_frequency=1,
            funding_currency="USD",
            card_present_acceptance_percent="100",
            internet_acceptance_percent="0",
            moto_acceptance_percent="0",
            business_email_address="business_email_address_example",
            business_website_url="business@email.com",
            customer_service_phone=PhoneNumber(
                intl_code="44",
                area_code="111",
                number="1231234",
                extension="2",
            ),
            not_present_delay_days=0,
            deposit_frequency="0",
            deposit_size_percent="1",
            deposit_balance_days="1",
            deposit_fulfillment_days="1",
            full_payment_percent="1",
            full_payment_fulfillment="1",
            utilize_cvv2=True,
            recurring_transactions=True,
            contract_term_type="ZERO_MONTH",
            months_closed=[
                "JAN",
            ],
            monetary_billing_method="CARD_DISCOUNT",
            authorization_included=True,
            annual_fee_month_start="JAN",
            money_services=True,
            payment_services=True,
            third_party_processor=True,
            non_government_non_profit=True,
            daily_discount=True,
            non_bank_atm=True,
            embassy=True,
            high_inter_annual_trans_ngo=True,
        ),
        sales_rep_code="12345",
        additional_shareholders=[
            Person(
                name=Name(
                    salutation="MR",
                    first_name="John",
                    middle_name="Lee",
                    last_name="Doe",
                ),
                contact_info=ContactInfo(
                    address=Address(
                        street_name="Baker Street",
                        street_number="221",
                        line_two="Apt B",
                        line_three="48",
                        city="Atlanta",
                        county="Fulton",
                        post_code="30346",
                        country="USA",
                        state="USA_AL",
                        classification="BUSINESS_STREET_ADDRESS",
                        contact_name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        location_name="Baker Plaza",
                    ),
                    additional_addresses={
                        "key": Address(
                            street_name="Baker Street",
                            street_number="221",
                            line_two="Apt B",
                            line_three="48",
                            city="Atlanta",
                            county="Fulton",
                            post_code="30346",
                            country="USA",
                            state="USA_AL",
                            classification="BUSINESS_STREET_ADDRESS",
                            contact_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            location_name="Baker Plaza",
                        ),
                    },
                    phone=PhoneNumber(
                        intl_code="44",
                        area_code="111",
                        number="1231234",
                        extension="2",
                    ),
                    mobile=PhoneNumber(
                        intl_code="44",
                        area_code="111",
                        number="1231234",
                        extension="2",
                    ),
                    fax=PhoneNumber(
                        intl_code="44",
                        area_code="111",
                        number="1231234",
                        extension="2",
                    ),
                    email_address="contactname@email.com",
                ),
                dob=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                positions={
                    "key": True,
                },
                ownership_pct="90",
                ids=[
                    Identification(
                        id_type="PASSPORT",
                        id_number="123456789",
                        expiry_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        issue_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        issuing_country="USA",
                        issuing_state="USA_AL",
                        id_name="id_name_example",
                        issuing_agency="issuing_agency_example",
                    ),
                ],
                title_type="ACCOUNTING_MANAGER",
                title="Chief Technology Officer",
                signing_personal_guarantee=True,
                responsible_party=True,
                related_party=True,
                residing_country="GBR",
                primary_nationality="GBR",
                secondary_nationality="IRL",
                documentary_info=DocumentaryInfo(
                    documentary=True,
                    documentary_verifier="SALES_TEAM",
                    documentary_issuer="USA",
                    documentary_type="DRIVER_LICENSE",
                    id_number="111111117",
                    issue_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    expiry_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    issuing_state="USA_AL",
                    foreign_issuing_state="foreign_issuing_state_example",
                ),
                alternate_address_info=AlternateAddressInfo(
                    document_needed=True,
                    document_verified=True,
                    alternate_address_document_type="BANK_STATEMENT",
                    document_name="document_name_example",
                ),
                is_new_owner=True,
                directional_ownership_type="DIRECT_OWNERSHIP",
                signing_agreement=True,
                us_person=True,
            ),
        ],
        contact=Person(
            name=Name(
                salutation="MR",
                first_name="John",
                middle_name="Lee",
                last_name="Doe",
            ),
            contact_info=ContactInfo(
                address=Address(
                    street_name="Baker Street",
                    street_number="221",
                    line_two="Apt B",
                    line_three="48",
                    city="Atlanta",
                    county="Fulton",
                    post_code="30346",
                    country="USA",
                    state="USA_AL",
                    classification="BUSINESS_STREET_ADDRESS",
                    contact_name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    location_name="Baker Plaza",
                ),
                additional_addresses={
                    "key": Address(
                        street_name="Baker Street",
                        street_number="221",
                        line_two="Apt B",
                        line_three="48",
                        city="Atlanta",
                        county="Fulton",
                        post_code="30346",
                        country="USA",
                        state="USA_AL",
                        classification="BUSINESS_STREET_ADDRESS",
                        contact_name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        location_name="Baker Plaza",
                    ),
                },
                phone=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                mobile=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                fax=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                email_address="contactname@email.com",
            ),
            dob=DateComponents(
                year=1970,
                month="JAN",
                day=15,
            ),
            positions={
                "key": True,
            },
            ownership_pct="90",
            ids=[
                Identification(
                    id_type="PASSPORT",
                    id_number="123456789",
                    expiry_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    issue_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    issuing_country="USA",
                    issuing_state="USA_AL",
                    id_name="id_name_example",
                    issuing_agency="issuing_agency_example",
                ),
            ],
            title_type="ACCOUNTING_MANAGER",
            title="Chief Technology Officer",
            signing_personal_guarantee=True,
            responsible_party=True,
            related_party=True,
            residing_country="GBR",
            primary_nationality="GBR",
            secondary_nationality="IRL",
            documentary_info=DocumentaryInfo(
                documentary=True,
                documentary_verifier="SALES_TEAM",
                documentary_issuer="USA",
                documentary_type="DRIVER_LICENSE",
                id_number="111111117",
                issue_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                expiry_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                issuing_state="USA_AL",
                foreign_issuing_state="foreign_issuing_state_example",
            ),
            alternate_address_info=AlternateAddressInfo(
                document_needed=True,
                document_verified=True,
                alternate_address_document_type="BANK_STATEMENT",
                document_name="document_name_example",
            ),
            is_new_owner=True,
            directional_ownership_type="DIRECT_OWNERSHIP",
            signing_agreement=True,
            us_person=True,
        ),
        bank_accounts={
            "key": BankingInfo(
                account_name="John Doe",
                bank_name="Wells Fargo",
                urgent_payment=True,
                funding_method="NETCREDIT",
                account_number="20581687",
                sort_code="121000248",
                iban="GB48LOYD3037341",
                swift_code="CPRTGB22",
                bank_creditor_id="bank_creditor_id_example",
                bank_direct=True,
                country="GBR",
                tape_id="14",
                true_daily=True,
                use_chain_account_number=True,
            ),
        },
        card_pricing=CardPricing(
            pricing_method="CLEAR_AND_SIMPLE",
            pricing_category="RETAIL",
            amex_accepting_info=AmexAcceptingInfo(
                amex_monthly_card_sales=3553.0,
                is_existing=True,
                amex_mid="2101491576",
            ),
            payment_facilitator_info=PaymentFacilitatorInfo(
                payment_facilitator_type="PAYMENT_FACILITATOR",
                card_prefixes=[
                    CardPrefix(
                        card_type="VISA",
                        prefix="DE",
                    ),
                ],
            ),
            card_charges=[
                CardCharge(
                    card_type="VISA",
                    minimum_fee=0.03,
                    authorization_fee=3.14,
                    se_number="123456789",
                    service_type="PARTIAL_SERVICE",
                    card_funding="ELAVON",
                    pricing_tiers={
                        "key": PricingTier(
                            discount_rate=2.0,
                            discount_per_item=0.2,
                        ),
                    },
                ),
            ],
            exception_charges=[
                ExceptionCharge(
                    type="BUSINESS_CARDS",
                    discount_rate=1.0,
                    discount_per_item=0.1,
                ),
            ],
            debit_pricing=DebitPricing(
                pricing_method="INTERCHANGE_DIFFERENTIAL",
                authorization_method="FIXED",
                surcharge_amount=1.1,
                surcharge_percent="0.1",
                debit_network_charges=[
                    DebitNetworkCharge(
                        type="INTERLINK",
                        discount_rate=5.0,
                        discount_per_item=0.5,
                        per_auth=3.14,
                    ),
                ],
                pinless_setup=True,
            ),
        ),
        fees=[
            Fee(
                type="JOI",
                quantity=1,
                amount=9.99,
                frequency="ANNUAL",
                start_month="JAN",
            ),
        ],
        monetary_pricing_program="monetary_pricing_program_example",
        authenticate_pricing_program="47777",
        parent_entity="parent_entity_example",
        short_name="MS00EPNA",
        fraud_check_result=FraudCheckResult(
            transaction_id="1100000000540130",
            decision="PASS",
        ),
        site_survey=SiteSurvey(
            site_survey_conducted=True,
            location_type="SHOPPING_CENTRE",
            site_address_same_as_dba=True,
            location_environment="BUSINESS_DISTRICT",
            vicinity_condition="WELL_KEPT",
            location_square_meters="LTE_TO_250",
            location_appearance="VERY_GOOD",
            business_operating=True,
            inventory_display_adequate=True,
            inventory_consistent_with_business_type=True,
            card_decals_visible=True,
            card_decals_installed_at_visit=True,
        ),
        dynamic_currency_conversion=DynamicCurrencyConversion(
            rebate_percent=0.5,
            mark_up="ZERO",
            currency_group="FIVE_USD_DCC_CURRENCIES",
            registration_fee=2.0,
        ),
        billing_statement=BillingStatement(
            type="SURCHARGE_TIERED",
            media="DYNAMIC_MERCHANT_REPORTING",
            address_type="BUSINESS",
            email_address="applicantname@email.com",
            frequency="DAILY",
        ),
        funding_statement=FundingStatement(
            type="SURCHARGE_TIERED",
            media="DYNAMIC_MERCHANT_REPORTING",
            email_address="applicant@email.com",
            frequency="DAILY",
        ),
        electronic_statement=ElectronicStatement(
            type="SURCHARGE_TIERED",
            media="DYNAMIC_MERCHANT_REPORTING",
            email_address="applicant@email.com",
            frequency="DAILY",
        ),
        vat_invoice_statement=VatInvoiceStatement(
            type="SURCHARGE_TIERED",
            media="DYNAMIC_MERCHANT_REPORTING",
            address_type="BUSINESS",
        ),
        billing_method="NETCREDIT",
        referrer_name="PARTNER_BANK",
        referrer_reference_number="11",
        previous_processor="previous_processor_example",
        value_added_info=ValueAddedInfo(
            value_adds={
                "key": True,
            },
            ebt_info=EbtInfo(
                se_number="123456789",
                authorization_fee=0.03,
            ),
            ecs_info=EcsInfo(
                processing_acceptance_type="POP_POS_IMAGE",
                service_level_type="GUARANTEE_WITH_VERIFY",
                annual_check_volume=100000.0,
                average_check_amount=25.0,
                max_check_amount=1000,
                per_transaction=0.0,
                discount_rate=0.0,
                monthly_minimum=0.0,
                per_return_fee=0.0,
                nsf_service_processing_fee=0.0,
                nsf_service_fee=0.0,
                collection=True,
                enquire_reporting=True,
                service_provider_type="ENCIRCLE_DIRECT",
            ),
            acs_info=AcsInfo(
                reporting_id="reporting_id_example",
            ),
            fanfare_info=FanfareInfo(
                max_card_value="max_card_value_example",
                package_type="STANDARD_GIFT_LOYALTY",
                enrollment={
                    "key": EnrollmentInfo(
                        discount_rate=0.0,
                        discount_amount=0.0,
                    ),
                },
                loyalty={
                    "key": LoyaltyInfo(
                        visits=1,
                        amount_spent=22.0,
                        discount_rate=1.1,
                        discount_amount=5.0,
                    ),
                },
            ),
            gsm_prepaid_type="EURONET_NO_PAYS",
            surcharge_managed_by="surcharge_managed_by_example",
            credit_surcharge_amt="credit_surcharge_amt_example",
            efs3d_secure_info=Efs3dSecureInfo(
                billing_per_item_fee=3.14,
            ),
            straight_send_info=StraightSendInfo(
                per_transaction_fee=3.14,
                percent_fee=3.14,
            ),
            on_demand_info=OnDemandInfo(
                per_transaction_fee=3.14,
                percent_fee=3.14,
            ),
            ocm_info=OcmInfo(
                setup_type="Mid, Chain",
                setup_fee=0.0,
                monthly_fee=0.0,
                number_of_users=1,
            ),
        ),
        equipment_info=EquipmentInfo(
            equipment_items=[
                EquipmentItem(
                    code="310T3",
                    quantity=2,
                    pricing_items=[
                        EquipmentPricing(
                            amount=200.0,
                            purchase_type="EXCHANGE",
                            lease_term=1,
                            vendor_code=1,
                            vendor_plan="vendor_plan_example",
                            start_month="JAN",
                            start_year="2010",
                        ),
                    ],
                    item_settings=ItemSettings(
                        security_level="BASIC",
                        semi_integrated=True,
                        connection_type="STANDARD_IP",
                        close_method="MANUAL",
                        capture_method="HOST",
                        qir_vendor="qir_vendor_example",
                        services={
                            "key": True,
                        },
                        options=[
                            EquipmentOption(
                                integrator_code="integrator_code_example",
                                ciers_number="ciers_number_example",
                                serial_number="serial_number_example",
                                model_number="model_number_example",
                                ecr_type="SMARTLINK",
                                ecr_mode="LITE_TOUCH",
                                print_via_ecr=True,
                                ecr_integrator="ALMAR",
                                ecr_cable_type="NONE",
                                epg_integration_type="REMOTE",
                                bax_number="bax_number_example",
                                bax_effective_date=DateComponents(
                                    year=1970,
                                    month="JAN",
                                    day=15,
                                ),
                            ),
                        ],
                        bundled_thresh_hold=1,
                        service_pricing_code="CORE",
                        terminal_type="INTERNET",
                        ingenico_pay_table=True,
                        deploy_type="DEPLOY",
                    ),
                    exception_items=[
                        ExceptionItem(
                            type="type_example",
                            discount_rate=3.14,
                            discount_per_item=3.14,
                        ),
                    ],
                    service_fee=3.14,
                    trx_free_month=1,
                    future_effective_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                ),
            ],
            terminal_services=[
                TerminalService(
                    type="QUICK_CLOSE",
                    service_specifics="service_specifics_example",
                ),
            ],
            training_type="TRAINING",
            shipping_method="NEXT_DAY",
            network="ELAVON",
            fusebox_info=FuseboxInfo(
                simplify_quantity=1,
                direct_quantity=1,
                simplify_location="simplify_location_example",
                direct_to_fusebox_location="direct_to_fusebox_location_example",
            ),
            anticipated_start_date=DateComponents(
                year=1970,
                month="JAN",
                day=15,
            ),
        ),
        branch_number="111",
        branch_code="1234",
        self_boarded_external=True,
        employee_number="11222",
        rep_referral_number="321",
        promotional_code="00001",
        chain_info=ChainInfo(
            chain_number="chain_number_example",
            chain_name="chain_name_example",
            send_statement_to_address="BUSINESS",
            statement_media="DYNAMIC_MERCHANT_REPORTING",
            address=Address(
                street_name="Baker Street",
                street_number="221",
                line_two="Apt B",
                line_three="48",
                city="Atlanta",
                county="Fulton",
                post_code="30346",
                country="USA",
                state="USA_AL",
                classification="BUSINESS_STREET_ADDRESS",
                contact_name=Name(
                    salutation="MR",
                    first_name="John",
                    middle_name="Lee",
                    last_name="Doe",
                ),
                location_name="Baker Plaza",
            ),
            chain_level_billing=True,
            bank_accounts={
                "key": BankingInfo(
                    account_name="John Doe",
                    bank_name="Wells Fargo",
                    urgent_payment=True,
                    funding_method="NETCREDIT",
                    account_number="20581687",
                    sort_code="121000248",
                    iban="GB48LOYD3037341",
                    swift_code="CPRTGB22",
                    bank_creditor_id="bank_creditor_id_example",
                    bank_direct=True,
                    country="GBR",
                    tape_id="14",
                    true_daily=True,
                    use_chain_account_number=True,
                ),
            },
        ),
        distributions={
            "key": DistributionInfo(
                method="MAILING",
                address_type="BUSINESS",
                email_address="applicant@email.com",
            ),
        },
        additional_location_info=AdditionalLocationInfo(
            central_mid="8024999222",
            central_legal_name="Elavon",
            central_tax_id="787421357",
        ),
        signed_date=DateComponents(
            year=1970,
            month="JAN",
            day=15,
        ),
        signed_type="WET",
        intermediary_owner_info=IntermediaryOwnerInfo(
            intermediary_owners=[
                IntermediaryOwner(
                    ownership_pct="90",
                    business_name="ACME",
                    owner_name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    phone=PhoneNumber(
                        intl_code="44",
                        area_code="111",
                        number="1231234",
                        extension="2",
                    ),
                    email_address="email_address_example",
                    address=Address(
                        street_name="Baker Street",
                        street_number="221",
                        line_two="Apt B",
                        line_three="48",
                        city="Atlanta",
                        county="Fulton",
                        post_code="30346",
                        country="USA",
                        state="USA_AL",
                        classification="BUSINESS_STREET_ADDRESS",
                        contact_name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        location_name="Baker Plaza",
                    ),
                ),
            ],
            additional_intermediate_owners=True,
        ),
        revenue_share_info=RevenueShareInfo(
            secondary_sales_person="12345",
            split_percentage="50",
        ),
        elavon_contract="UK",
        internal_use_info=InternalUseInfo(
            field_auto_info=FieldAutoInfo(
                requested=True,
                applied=True,
                monitored=True,
                values_modified=True,
                field_auto_reference_id="field_auto_reference_id_example",
            ),
            sales_rep_info=SalesRepInfo(
                sales_rep_code="12345",
                name="name_example",
                email="repname@email.com",
                submitted=True,
            ),
            tin_applied_to_all=True,
            ip_address="ip_address_example",
        ),
        eframe_info=EframeInfo(
            scheme_selection="scheme_selection_example",
            pos_contract=True,
            is_girocard=True,
        ),
        partner_info=PartnerInfo(
            partner_name="partner_name_example",
            associate_id="associate_id_example",
            book_of_business="book_of_business_example",
            correlation_id="correlation_id_example",
            partner_source="partner_source_example",
            merchant_user_id="merchant_user_id_example",
            session_id="session_id_example",
        ),
        alternative_payment_methods=[
            ApmAcquirer(
                acquirer_code="acquirer_code_example",
                acquirer_types=[
                    ApmAcquirerType(
                        type_code="type_code_example",
                        per_item_amount="per_item_amount_example",
                        rate_percentage="rate_percentage_example",
                        pricing_tiers=[
                            ApmPricingTier(
                                combining_code="combining_code_example",
                                per_item_amount="per_item_amount_example",
                                rate_percentage="rate_percentage_example",
                                description="description_example",
                            ),
                        ],
                    ),
                ],
            ),
        ],
    ) # ScarecrowApplication | 

    # example passing only required values which don't have defaults set
    try:
        # Credit Check
        api_response = api_instance.credit_check(version_number, body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->credit_check: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_number** | **int**|  |
 **body** | [**ScarecrowApplication**](ScarecrowApplication.md)|  |

### Return type

[**CreditCheckResponse**](CreditCheckResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Credit Check Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_check_xsd_schema**
> credit_check_xsd_schema(version_number, iso3_country)

Get Credit Check Schema

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    version_number = 1 # int | 
    iso3_country = "iso3Country_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Credit Check Schema
        api_instance.credit_check_xsd_schema(version_number, iso3_country)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->credit_check_xsd_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_number** | **int**|  |
 **iso3_country** | **str**|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_packet**
> DeleteDocumentPacketResponse delete_document_packet(body)

Delete a Document Packet

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.delete_document_packet_request import DeleteDocumentPacketRequest
from elavon.model.delete_document_packet_response import DeleteDocumentPacketResponse
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = DeleteDocumentPacketRequest(
        document_packet_id="document_packet_id_example",
    ) # DeleteDocumentPacketRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a Document Packet
        api_response = api_instance.delete_document_packet(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->delete_document_packet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteDocumentPacketRequest**](DeleteDocumentPacketRequest.md)|  |

### Return type

[**DeleteDocumentPacketResponse**](DeleteDocumentPacketResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Delete a Document Packet Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_document_packet**
> DeleteGroupDocumentPacketResponse delete_group_document_packet(body)

Delete Group Document Packet

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.delete_group_document_packet_response import DeleteGroupDocumentPacketResponse
from elavon.model.delete_group_document_packet_request import DeleteGroupDocumentPacketRequest
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = DeleteGroupDocumentPacketRequest(
        group_document_packet_id="group_document_packet_id_example",
    ) # DeleteGroupDocumentPacketRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Group Document Packet
        api_response = api_instance.delete_group_document_packet(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->delete_group_document_packet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteGroupDocumentPacketRequest**](DeleteGroupDocumentPacketRequest.md)|  |

### Return type

[**DeleteGroupDocumentPacketResponse**](DeleteGroupDocumentPacketResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Delete Group DocumentPacket |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_group_document_packet**
> ExecuteGroupDocumentPacketResponse execute_group_document_packet(body)

Execute Document Packet

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.execute_group_document_packet_request import ExecuteGroupDocumentPacketRequest
from elavon.model.execute_group_document_packet_response import ExecuteGroupDocumentPacketResponse
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = ExecuteGroupDocumentPacketRequest(
        group_document_packet_id="group_document_packet_id_example",
    ) # ExecuteGroupDocumentPacketRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Execute Document Packet
        api_response = api_instance.execute_group_document_packet(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->execute_group_document_packet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExecuteGroupDocumentPacketRequest**](ExecuteGroupDocumentPacketRequest.md)|  |

### Return type

[**ExecuteGroupDocumentPacketResponse**](ExecuteGroupDocumentPacketResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Execute Group Document Packet Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_packet_documents**
> GeneratePacketDocumentsResponse generate_packet_documents(body)

Trigger generation of document in packet for submission

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.generate_packet_documents_request import GeneratePacketDocumentsRequest
from elavon.model.generate_packet_documents_response import GeneratePacketDocumentsResponse
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = GeneratePacketDocumentsRequest(
        document_packet_id="document_packet_id_example",
    ) # GeneratePacketDocumentsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Trigger generation of document in packet for submission
        api_response = api_instance.generate_packet_documents(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->generate_packet_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GeneratePacketDocumentsRequest**](GeneratePacketDocumentsRequest.md)|  |

### Return type

[**GeneratePacketDocumentsResponse**](GeneratePacketDocumentsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Generate Packet Documents Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_presented_documents**
> GetDocumentsResponse get_presented_documents(body)

Get all documents to present to the user

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.get_documents_request import GetDocumentsRequest
from elavon.model.get_documents_response import GetDocumentsResponse
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = GetDocumentsRequest(
        profile_code="TEST",
        document_inputs={
            "key": UserDocumentInput(
                language="en",
                document_id="1",
                agreement_id="2101491576",
                document_packet_id="42f441d0-0c23-468d-8319-f1e2af17dc15",
                signed=True,
                grouped_application=True,
                wet_signed=True,
            ),
        },
        html=True,
    ) # GetDocumentsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get all documents to present to the user
        api_response = api_instance.get_presented_documents(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->get_presented_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetDocumentsRequest**](GetDocumentsRequest.md)|  |

### Return type

[**GetDocumentsResponse**](GetDocumentsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Get Presented Documents Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quiz**
> GetQuizResponse get_quiz(version_number, body)

Request KYC Quiz

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.get_quiz_response import GetQuizResponse
from elavon.model.get_quiz_request import GetQuizRequest
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    version_number = 1 # int | 
    body = GetQuizRequest(
        principal=Person(
            name=Name(
                salutation="MR",
                first_name="John",
                middle_name="Lee",
                last_name="Doe",
            ),
            contact_info=ContactInfo(
                address=Address(
                    street_name="Baker Street",
                    street_number="221",
                    line_two="Apt B",
                    line_three="48",
                    city="Atlanta",
                    county="Fulton",
                    post_code="30346",
                    country="USA",
                    state="USA_AL",
                    classification="BUSINESS_STREET_ADDRESS",
                    contact_name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    location_name="Baker Plaza",
                ),
                additional_addresses={
                    "key": Address(
                        street_name="Baker Street",
                        street_number="221",
                        line_two="Apt B",
                        line_three="48",
                        city="Atlanta",
                        county="Fulton",
                        post_code="30346",
                        country="USA",
                        state="USA_AL",
                        classification="BUSINESS_STREET_ADDRESS",
                        contact_name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        location_name="Baker Plaza",
                    ),
                },
                phone=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                mobile=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                fax=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                email_address="contactname@email.com",
            ),
            dob=DateComponents(
                year=1970,
                month="JAN",
                day=15,
            ),
            positions={
                "key": True,
            },
            ownership_pct="90",
            ids=[
                Identification(
                    id_type="PASSPORT",
                    id_number="123456789",
                    expiry_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    issue_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    issuing_country="USA",
                    issuing_state="USA_AL",
                    id_name="id_name_example",
                    issuing_agency="issuing_agency_example",
                ),
            ],
            title_type="ACCOUNTING_MANAGER",
            title="Chief Technology Officer",
            signing_personal_guarantee=True,
            responsible_party=True,
            related_party=True,
            residing_country="GBR",
            primary_nationality="GBR",
            secondary_nationality="IRL",
            documentary_info=DocumentaryInfo(
                documentary=True,
                documentary_verifier="SALES_TEAM",
                documentary_issuer="USA",
                documentary_type="DRIVER_LICENSE",
                id_number="111111117",
                issue_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                expiry_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                issuing_state="USA_AL",
                foreign_issuing_state="foreign_issuing_state_example",
            ),
            alternate_address_info=AlternateAddressInfo(
                document_needed=True,
                document_verified=True,
                alternate_address_document_type="BANK_STATEMENT",
                document_name="document_name_example",
            ),
            is_new_owner=True,
            directional_ownership_type="DIRECT_OWNERSHIP",
            signing_agreement=True,
            us_person=True,
        ),
        business_address=Address(
            street_name="Baker Street",
            street_number="221",
            line_two="Apt B",
            line_three="48",
            city="Atlanta",
            county="Fulton",
            post_code="30346",
            country="USA",
            state="USA_AL",
            classification="BUSINESS_STREET_ADDRESS",
            contact_name=Name(
                salutation="MR",
                first_name="John",
                middle_name="Lee",
                last_name="Doe",
            ),
            location_name="Baker Plaza",
        ),
        language="en",
    ) # GetQuizRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Request KYC Quiz
        api_response = api_instance.get_quiz(version_number, body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->get_quiz: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_number** | **int**|  |
 **body** | [**GetQuizRequest**](GetQuizRequest.md)|  |

### Return type

[**GetQuizResponse**](GetQuizResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Get Quiz Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quiz_xsd_schema**
> get_quiz_xsd_schema(version_number)

Get Quiz Request Schema

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    version_number = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get Quiz Request Schema
        api_instance.get_quiz_xsd_schema(version_number)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->get_quiz_xsd_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_number** | **int**|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signed_document_packet_content**
> GetDocumentsResponse get_signed_document_packet_content(body)

Get signed document packet content

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.get_documents_response import GetDocumentsResponse
from elavon.model.get_signed_document_packet_request import GetSignedDocumentPacketRequest
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = GetSignedDocumentPacketRequest(
        document_packet_id="42f441d0-0c23-468d-8319-f1e2af17dc15",
    ) # GetSignedDocumentPacketRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get signed document packet content
        api_response = api_instance.get_signed_document_packet_content(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->get_signed_document_packet_content: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetSignedDocumentPacketRequest**](GetSignedDocumentPacketRequest.md)|  |

### Return type

[**GetDocumentsResponse**](GetDocumentsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Get Unsiged Document Packet Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_terminal_ids**
> GetTerminalIdsResponse get_terminal_ids(body)

Get terminal ids and related information for MID

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.get_terminal_ids_request import GetTerminalIdsRequest
from elavon.model.get_terminal_ids_response import GetTerminalIdsResponse
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = GetTerminalIdsRequest(
        mid="8024999222",
        unique_id="8024999223",
    ) # GetTerminalIdsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get terminal ids and related information for MID
        api_response = api_instance.get_terminal_ids(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->get_terminal_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetTerminalIdsRequest**](GetTerminalIdsRequest.md)|  |

### Return type

[**GetTerminalIdsResponse**](GetTerminalIdsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Get Terminal Ids |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unsigned_document_content**
> GetDocumentResponse get_unsigned_document_content(body)

Get unsigned document packet singular document

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.get_document_response import GetDocumentResponse
from elavon.model.get_unsigned_document_request import GetUnsignedDocumentRequest
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = GetUnsignedDocumentRequest(
        document_packet_id="42f441d0-0c23-468d-8319-f1e2af17dc15",
        html=True,
        code="OPERATING_GUIDE",
        cardinal_number=1,
    ) # GetUnsignedDocumentRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get unsigned document packet singular document
        api_response = api_instance.get_unsigned_document_content(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->get_unsigned_document_content: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetUnsignedDocumentRequest**](GetUnsignedDocumentRequest.md)|  |

### Return type

[**GetDocumentResponse**](GetDocumentResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Get Unsiged Document Packet Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unsigned_documents_packet_content**
> GetDocumentsResponse get_unsigned_documents_packet_content(body)

Get unsigned document packet full content

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.get_documents_response import GetDocumentsResponse
from elavon.model.get_unsigned_documents_packet_request import GetUnsignedDocumentsPacketRequest
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = GetUnsignedDocumentsPacketRequest(
        document_packet_id="42f441d0-0c23-468d-8319-f1e2af17dc15",
        html=True,
    ) # GetUnsignedDocumentsPacketRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get unsigned document packet full content
        api_response = api_instance.get_unsigned_documents_packet_content(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->get_unsigned_documents_packet_content: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetUnsignedDocumentsPacketRequest**](GetUnsignedDocumentsPacketRequest.md)|  |

### Return type

[**GetDocumentsResponse**](GetDocumentsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Get Unsiged Document Packet Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_packet_presented_documents**
> ListDocumentsResponse list_packet_presented_documents(body)

List Packet Documents to present to the user

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.list_packet_documents_request import ListPacketDocumentsRequest
from elavon.model.list_documents_response import ListDocumentsResponse
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = ListPacketDocumentsRequest(
        document_packet_id="document_packet_id_example",
    ) # ListPacketDocumentsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List Packet Documents to present to the user
        api_response = api_instance.list_packet_presented_documents(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->list_packet_presented_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListPacketDocumentsRequest**](ListPacketDocumentsRequest.md)|  |

### Return type

[**ListDocumentsResponse**](ListDocumentsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard List  Packet Presented Documents Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_presented_documents**
> ListDocumentsResponse list_presented_documents(body)

List Documents to present to the user

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.list_documents_request import ListDocumentsRequest
from elavon.model.list_documents_response import ListDocumentsResponse
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = ListDocumentsRequest(
        equipment_info=EquipmentInfo(
            equipment_items=[
                EquipmentItem(
                    code="310T3",
                    quantity=2,
                    pricing_items=[
                        EquipmentPricing(
                            amount=200.0,
                            purchase_type="EXCHANGE",
                            lease_term=1,
                            vendor_code=1,
                            vendor_plan="vendor_plan_example",
                            start_month="JAN",
                            start_year="2010",
                        ),
                    ],
                    item_settings=ItemSettings(
                        security_level="BASIC",
                        semi_integrated=True,
                        connection_type="STANDARD_IP",
                        close_method="MANUAL",
                        capture_method="HOST",
                        qir_vendor="qir_vendor_example",
                        services={
                            "key": True,
                        },
                        options=[
                            EquipmentOption(
                                integrator_code="integrator_code_example",
                                ciers_number="ciers_number_example",
                                serial_number="serial_number_example",
                                model_number="model_number_example",
                                ecr_type="SMARTLINK",
                                ecr_mode="LITE_TOUCH",
                                print_via_ecr=True,
                                ecr_integrator="ALMAR",
                                ecr_cable_type="NONE",
                                epg_integration_type="REMOTE",
                                bax_number="bax_number_example",
                                bax_effective_date=DateComponents(
                                    year=1970,
                                    month="JAN",
                                    day=15,
                                ),
                            ),
                        ],
                        bundled_thresh_hold=1,
                        service_pricing_code="CORE",
                        terminal_type="INTERNET",
                        ingenico_pay_table=True,
                        deploy_type="DEPLOY",
                    ),
                    exception_items=[
                        ExceptionItem(
                            type="type_example",
                            discount_rate=3.14,
                            discount_per_item=3.14,
                        ),
                    ],
                    service_fee=3.14,
                    trx_free_month=1,
                    future_effective_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                ),
            ],
            terminal_services=[
                TerminalService(
                    type="QUICK_CLOSE",
                    service_specifics="service_specifics_example",
                ),
            ],
            training_type="TRAINING",
            shipping_method="NEXT_DAY",
            network="ELAVON",
            fusebox_info=FuseboxInfo(
                simplify_quantity=1,
                direct_quantity=1,
                simplify_location="simplify_location_example",
                direct_to_fusebox_location="direct_to_fusebox_location_example",
            ),
            anticipated_start_date=DateComponents(
                year=1970,
                month="JAN",
                day=15,
            ),
        ),
        card_pricing=CardPricing(
            pricing_method="CLEAR_AND_SIMPLE",
            pricing_category="RETAIL",
            amex_accepting_info=AmexAcceptingInfo(
                amex_monthly_card_sales=3553.0,
                is_existing=True,
                amex_mid="2101491576",
            ),
            payment_facilitator_info=PaymentFacilitatorInfo(
                payment_facilitator_type="PAYMENT_FACILITATOR",
                card_prefixes=[
                    CardPrefix(
                        card_type="VISA",
                        prefix="DE",
                    ),
                ],
            ),
            card_charges=[
                CardCharge(
                    card_type="VISA",
                    minimum_fee=0.03,
                    authorization_fee=3.14,
                    se_number="123456789",
                    service_type="PARTIAL_SERVICE",
                    card_funding="ELAVON",
                    pricing_tiers={
                        "key": PricingTier(
                            discount_rate=2.0,
                            discount_per_item=0.2,
                        ),
                    },
                ),
            ],
            exception_charges=[
                ExceptionCharge(
                    type="BUSINESS_CARDS",
                    discount_rate=1.0,
                    discount_per_item=0.1,
                ),
            ],
            debit_pricing=DebitPricing(
                pricing_method="INTERCHANGE_DIFFERENTIAL",
                authorization_method="FIXED",
                surcharge_amount=1.1,
                surcharge_percent="0.1",
                debit_network_charges=[
                    DebitNetworkCharge(
                        type="INTERLINK",
                        discount_rate=5.0,
                        discount_per_item=0.5,
                        per_auth=3.14,
                    ),
                ],
                pinless_setup=True,
            ),
        ),
        principal=Person(
            name=Name(
                salutation="MR",
                first_name="John",
                middle_name="Lee",
                last_name="Doe",
            ),
            contact_info=ContactInfo(
                address=Address(
                    street_name="Baker Street",
                    street_number="221",
                    line_two="Apt B",
                    line_three="48",
                    city="Atlanta",
                    county="Fulton",
                    post_code="30346",
                    country="USA",
                    state="USA_AL",
                    classification="BUSINESS_STREET_ADDRESS",
                    contact_name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    location_name="Baker Plaza",
                ),
                additional_addresses={
                    "key": Address(
                        street_name="Baker Street",
                        street_number="221",
                        line_two="Apt B",
                        line_three="48",
                        city="Atlanta",
                        county="Fulton",
                        post_code="30346",
                        country="USA",
                        state="USA_AL",
                        classification="BUSINESS_STREET_ADDRESS",
                        contact_name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        location_name="Baker Plaza",
                    ),
                },
                phone=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                mobile=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                fax=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                email_address="contactname@email.com",
            ),
            dob=DateComponents(
                year=1970,
                month="JAN",
                day=15,
            ),
            positions={
                "key": True,
            },
            ownership_pct="90",
            ids=[
                Identification(
                    id_type="PASSPORT",
                    id_number="123456789",
                    expiry_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    issue_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    issuing_country="USA",
                    issuing_state="USA_AL",
                    id_name="id_name_example",
                    issuing_agency="issuing_agency_example",
                ),
            ],
            title_type="ACCOUNTING_MANAGER",
            title="Chief Technology Officer",
            signing_personal_guarantee=True,
            responsible_party=True,
            related_party=True,
            residing_country="GBR",
            primary_nationality="GBR",
            secondary_nationality="IRL",
            documentary_info=DocumentaryInfo(
                documentary=True,
                documentary_verifier="SALES_TEAM",
                documentary_issuer="USA",
                documentary_type="DRIVER_LICENSE",
                id_number="111111117",
                issue_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                expiry_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                issuing_state="USA_AL",
                foreign_issuing_state="foreign_issuing_state_example",
            ),
            alternate_address_info=AlternateAddressInfo(
                document_needed=True,
                document_verified=True,
                alternate_address_document_type="BANK_STATEMENT",
                document_name="document_name_example",
            ),
            is_new_owner=True,
            directional_ownership_type="DIRECT_OWNERSHIP",
            signing_agreement=True,
            us_person=True,
        ),
        business_info=BusinessInfo(
            dba_name="Grimm's Bookstore",
            dba_name_extended="Grimm's Fairytales and Other Stories Bookstore",
            business_address=Address(
                street_name="Baker Street",
                street_number="221",
                line_two="Apt B",
                line_three="48",
                city="Atlanta",
                county="Fulton",
                post_code="30346",
                country="USA",
                state="USA_AL",
                classification="BUSINESS_STREET_ADDRESS",
                contact_name=Name(
                    salutation="MR",
                    first_name="John",
                    middle_name="Lee",
                    last_name="Doe",
                ),
                location_name="Baker Plaza",
            ),
            legal_name="Barkers Dog Bakery",
            legal_name_extended="Baking Better Biscuits for Your Favorite Barkers Dog Bakery LLC",
            legal_name_marked=[
                "legal_name_marked_example",
            ],
            additional_addresses={
                "key": Address(
                    street_name="Baker Street",
                    street_number="221",
                    line_two="Apt B",
                    line_three="48",
                    city="Atlanta",
                    county="Fulton",
                    post_code="30346",
                    country="USA",
                    state="USA_AL",
                    classification="BUSINESS_STREET_ADDRESS",
                    contact_name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    location_name="Baker Plaza",
                ),
            },
            ownership_type="SOLE_TRADER",
            registration_number="1234567",
            tax_id="787421357",
            tax_id_type="FEDERAL_TAX_ID",
            vat_info=VatInfo(
                number_option="VAT_NBR",
                number56_b="123456789",
                expiry_date56_b=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                tax_number_type="CORPORATE_TAX_NUMBER",
                tax_number="tax_number_example",
            ),
            tax_form_type="W9",
            tax_class_type="CORPORATION",
            customer_membership_number="111222",
            product_description="Bakeries",
            mcc_code="7399E",
            establishment_year="2005",
            current_ownership_years="3",
            current_ownership_months="6",
            government_owned_entity=True,
            communication_language="en",
            pos_language="en",
            store_number="123456789",
            association_codes=[
                "12345",
            ],
            opt_out=True,
            sign_date=DateComponents(
                year=1970,
                month="JAN",
                day=15,
            ),
            pci_info=PCIInfo(
                pci_program_level="ONE",
                pci_service_type="BASIC",
                pci_contact_first_name="pci_contact_first_name_example",
                pci_contact_last_name="pci_contact_last_name_example",
                pci_contact_email_address="pci_contact_email_address_example",
                pci_contact_phone=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                pci_groups=[
                    "PCI_PROGRAM_EXCLUSION",
                ],
            ),
            employer_id="1234567",
            country_of_origin="USA",
            exemption_type="ADDITIONAL_LOCATION",
            owner_exemption_type="BANK_ADVISED_POOLED",
            number_of_partners="ONE",
            relationship_mgr_code="1234567",
            country_of_primary_operation="USA",
            bearer_shares=True,
            legal_status="CERTIFIED_INCORPORATION_ARTICLES",
            verifications={
                "key": VerificationInfo(
                    documentary=True,
                    issuing_country="USA",
                    issuing_state="USA_AL",
                    site_person_met="John Smith",
                    site_visit_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    id_number="111111117",
                    issue_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    expiry_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    document_type="CERTIFIED_INCORPORATION_ARTICLES",
                ),
            },
            industry_class="LODGING",
            no_plates=True,
            agent_number="1223334",
            location_mid_range="NORDIC",
            hemp_grower_info=HempGrowerInfo(
                operations_description="operations_description_example",
                is_licensed=True,
                license_expiration_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                additional_mrb_activity=True,
                cannabis_revenue_percentage_range="NONE",
            ),
            credit_decision_info=CreditDecisionInfo(
                credit_decision_flag=True,
                credit_decision_id="credit_decision_id_example",
            ),
        ),
        bank_accounts={
            "key": BankingInfo(
                account_name="John Doe",
                bank_name="Wells Fargo",
                urgent_payment=True,
                funding_method="NETCREDIT",
                account_number="20581687",
                sort_code="121000248",
                iban="GB48LOYD3037341",
                swift_code="CPRTGB22",
                bank_creditor_id="bank_creditor_id_example",
                bank_direct=True,
                country="GBR",
                tape_id="14",
                true_daily=True,
                use_chain_account_number=True,
            ),
        },
        direct_debit_authorized_map={
            "key": True,
        },
        value_adds={
            "key": True,
        },
        profile_code="profile_code_example",
        has_government_incentive=True,
        has_custom_notes=True,
        partner_document_keys=[
            "partner_document_keys_example",
        ],
    ) # ListDocumentsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # List Documents to present to the user
        api_response = api_instance.list_presented_documents(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->list_presented_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListDocumentsRequest**](ListDocumentsRequest.md)|  |

### Return type

[**ListDocumentsResponse**](ListDocumentsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard List Presented Documents Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_code_xsd_schema**
> post_code_xsd_schema(version_number)

Get Postal Code Validation Schema

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    version_number = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get Postal Code Validation Schema
        api_instance.post_code_xsd_schema(version_number)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->post_code_xsd_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_number** | **int**|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postal_validate**
> ValidateZipCodeRequest postal_validate(version_number, body)

Validate Postal Code

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.validate_zip_code_request import ValidateZipCodeRequest
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    version_number = 1 # int | 
    body = ValidateZipCodeRequest(
        zip_code="20330",
        city="Arlington",
        country="USA",
    ) # ValidateZipCodeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Validate Postal Code
        api_response = api_instance.postal_validate(version_number, body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->postal_validate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_number** | **int**|  |
 **body** | [**ValidateZipCodeRequest**](ValidateZipCodeRequest.md)|  |

### Return type

[**ValidateZipCodeRequest**](ValidateZipCodeRequest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Validate ZipCode Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_signer_user_sessions**
> RefershSignerUserSessionsResponse refresh_signer_user_sessions(body)

Refresh the session for signers of a document packet

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.refersh_signer_user_sessions_response import RefershSignerUserSessionsResponse
from elavon.model.refresh_signer_users_sessions_request import RefreshSignerUsersSessionsRequest
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = RefreshSignerUsersSessionsRequest(
        document_packet_id="42f441d0-0c23-468d-8319-f1e2af17dc15",
        signer_ids=[
            "signer_ids_example",
        ],
    ) # RefreshSignerUsersSessionsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Refresh the session for signers of a document packet
        api_response = api_instance.refresh_signer_user_sessions(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->refresh_signer_user_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RefreshSignerUsersSessionsRequest**](RefreshSignerUsersSessionsRequest.md)|  |

### Return type

[**RefershSignerUserSessionsResponse**](RefershSignerUserSessionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of signer who&#39;s session was updated |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_packet_documents**
> Response regenerate_packet_documents(body)

Regenerate signed Packet Content in event of failure

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.regenerate_document_packet_request import RegenerateDocumentPacketRequest
from elavon.model.response import Response
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = RegenerateDocumentPacketRequest(
        document_packet_id="document_packet_id_example",
    ) # RegenerateDocumentPacketRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Regenerate signed Packet Content in event of failure
        api_response = api_instance.regenerate_packet_documents(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->regenerate_packet_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegenerateDocumentPacketRequest**](RegenerateDocumentPacketRequest.md)|  |

### Return type

[**Response**](Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document_packet**
> UpdateDocumentPacketResponse update_document_packet(body)

Update Document Packet

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.update_document_packet_request import UpdateDocumentPacketRequest
from elavon.model.update_document_packet_response import UpdateDocumentPacketResponse
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = UpdateDocumentPacketRequest(
        document_packet_id="document_packet_id_example",
        profile_code="profile_code_example",
        signers=[
            Signer(
                signer_id="signer_id_example",
                signer=Name(
                    salutation="MR",
                    first_name="John",
                    middle_name="Lee",
                    last_name="Doe",
                ),
                email_address="email_address_example",
                principal=True,
                signing_complete_url="signing_complete_url_example",
                signing_decline_url="signing_decline_url_example",
                signing_expired_url="signing_expired_url_example",
                language="language_example",
                opt_in_out1=True,
                opt_in_out2=True,
                opt_in_out3=True,
            ),
        ],
        document_packet_data=DocumentPacketData(
            scarecrow_application=ScarecrowApplication(
                client_id="IDNA",
                client_group_number="860",
                unique_id="AcmeCorp1572566399123",
                banker_id="123",
                banker_partner_id="123",
                country="USA",
                principal=Person(
                    name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    contact_info=ContactInfo(
                        address=Address(
                            street_name="Baker Street",
                            street_number="221",
                            line_two="Apt B",
                            line_three="48",
                            city="Atlanta",
                            county="Fulton",
                            post_code="30346",
                            country="USA",
                            state="USA_AL",
                            classification="BUSINESS_STREET_ADDRESS",
                            contact_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            location_name="Baker Plaza",
                        ),
                        additional_addresses={
                            "key": Address(
                                street_name="Baker Street",
                                street_number="221",
                                line_two="Apt B",
                                line_three="48",
                                city="Atlanta",
                                county="Fulton",
                                post_code="30346",
                                country="USA",
                                state="USA_AL",
                                classification="BUSINESS_STREET_ADDRESS",
                                contact_name=Name(
                                    salutation="MR",
                                    first_name="John",
                                    middle_name="Lee",
                                    last_name="Doe",
                                ),
                                location_name="Baker Plaza",
                            ),
                        },
                        phone=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        mobile=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        fax=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        email_address="contactname@email.com",
                    ),
                    dob=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    positions={
                        "key": True,
                    },
                    ownership_pct="90",
                    ids=[
                        Identification(
                            id_type="PASSPORT",
                            id_number="123456789",
                            expiry_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issue_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issuing_country="USA",
                            issuing_state="USA_AL",
                            id_name="id_name_example",
                            issuing_agency="issuing_agency_example",
                        ),
                    ],
                    title_type="ACCOUNTING_MANAGER",
                    title="Chief Technology Officer",
                    signing_personal_guarantee=True,
                    responsible_party=True,
                    related_party=True,
                    residing_country="GBR",
                    primary_nationality="GBR",
                    secondary_nationality="IRL",
                    documentary_info=DocumentaryInfo(
                        documentary=True,
                        documentary_verifier="SALES_TEAM",
                        documentary_issuer="USA",
                        documentary_type="DRIVER_LICENSE",
                        id_number="111111117",
                        issue_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        expiry_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        issuing_state="USA_AL",
                        foreign_issuing_state="foreign_issuing_state_example",
                    ),
                    alternate_address_info=AlternateAddressInfo(
                        document_needed=True,
                        document_verified=True,
                        alternate_address_document_type="BANK_STATEMENT",
                        document_name="document_name_example",
                    ),
                    is_new_owner=True,
                    directional_ownership_type="DIRECT_OWNERSHIP",
                    signing_agreement=True,
                    us_person=True,
                ),
                business_info=BusinessInfo(
                    dba_name="Grimm's Bookstore",
                    dba_name_extended="Grimm's Fairytales and Other Stories Bookstore",
                    business_address=Address(
                        street_name="Baker Street",
                        street_number="221",
                        line_two="Apt B",
                        line_three="48",
                        city="Atlanta",
                        county="Fulton",
                        post_code="30346",
                        country="USA",
                        state="USA_AL",
                        classification="BUSINESS_STREET_ADDRESS",
                        contact_name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        location_name="Baker Plaza",
                    ),
                    legal_name="Barkers Dog Bakery",
                    legal_name_extended="Baking Better Biscuits for Your Favorite Barkers Dog Bakery LLC",
                    legal_name_marked=[
                        "legal_name_marked_example",
                    ],
                    additional_addresses={
                        "key": Address(
                            street_name="Baker Street",
                            street_number="221",
                            line_two="Apt B",
                            line_three="48",
                            city="Atlanta",
                            county="Fulton",
                            post_code="30346",
                            country="USA",
                            state="USA_AL",
                            classification="BUSINESS_STREET_ADDRESS",
                            contact_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            location_name="Baker Plaza",
                        ),
                    },
                    ownership_type="SOLE_TRADER",
                    registration_number="1234567",
                    tax_id="787421357",
                    tax_id_type="FEDERAL_TAX_ID",
                    vat_info=VatInfo(
                        number_option="VAT_NBR",
                        number56_b="123456789",
                        expiry_date56_b=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        tax_number_type="CORPORATE_TAX_NUMBER",
                        tax_number="tax_number_example",
                    ),
                    tax_form_type="W9",
                    tax_class_type="CORPORATION",
                    customer_membership_number="111222",
                    product_description="Bakeries",
                    mcc_code="7399E",
                    establishment_year="2005",
                    current_ownership_years="3",
                    current_ownership_months="6",
                    government_owned_entity=True,
                    communication_language="en",
                    pos_language="en",
                    store_number="123456789",
                    association_codes=[
                        "12345",
                    ],
                    opt_out=True,
                    sign_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    pci_info=PCIInfo(
                        pci_program_level="ONE",
                        pci_service_type="BASIC",
                        pci_contact_first_name="pci_contact_first_name_example",
                        pci_contact_last_name="pci_contact_last_name_example",
                        pci_contact_email_address="pci_contact_email_address_example",
                        pci_contact_phone=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        pci_groups=[
                            "PCI_PROGRAM_EXCLUSION",
                        ],
                    ),
                    employer_id="1234567",
                    country_of_origin="USA",
                    exemption_type="ADDITIONAL_LOCATION",
                    owner_exemption_type="BANK_ADVISED_POOLED",
                    number_of_partners="ONE",
                    relationship_mgr_code="1234567",
                    country_of_primary_operation="USA",
                    bearer_shares=True,
                    legal_status="CERTIFIED_INCORPORATION_ARTICLES",
                    verifications={
                        "key": VerificationInfo(
                            documentary=True,
                            issuing_country="USA",
                            issuing_state="USA_AL",
                            site_person_met="John Smith",
                            site_visit_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            id_number="111111117",
                            issue_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            expiry_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            document_type="CERTIFIED_INCORPORATION_ARTICLES",
                        ),
                    },
                    industry_class="LODGING",
                    no_plates=True,
                    agent_number="1223334",
                    location_mid_range="NORDIC",
                    hemp_grower_info=HempGrowerInfo(
                        operations_description="operations_description_example",
                        is_licensed=True,
                        license_expiration_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        additional_mrb_activity=True,
                        cannabis_revenue_percentage_range="NONE",
                    ),
                    credit_decision_info=CreditDecisionInfo(
                        credit_decision_flag=True,
                        credit_decision_id="credit_decision_id_example",
                    ),
                ),
                financial_info=FinancialInfo(
                    avg_sale_amount="125",
                    monthly_card_sales="1000",
                    annual_card_sales="12000",
                    annual_revenue="240000",
                    highest_ticket_amount="1000",
                    highest_ticket_frequency=1,
                    funding_currency="USD",
                    card_present_acceptance_percent="100",
                    internet_acceptance_percent="0",
                    moto_acceptance_percent="0",
                    business_email_address="business_email_address_example",
                    business_website_url="business@email.com",
                    customer_service_phone=PhoneNumber(
                        intl_code="44",
                        area_code="111",
                        number="1231234",
                        extension="2",
                    ),
                    not_present_delay_days=0,
                    deposit_frequency="0",
                    deposit_size_percent="1",
                    deposit_balance_days="1",
                    deposit_fulfillment_days="1",
                    full_payment_percent="1",
                    full_payment_fulfillment="1",
                    utilize_cvv2=True,
                    recurring_transactions=True,
                    contract_term_type="ZERO_MONTH",
                    months_closed=[
                        "JAN",
                    ],
                    monetary_billing_method="CARD_DISCOUNT",
                    authorization_included=True,
                    annual_fee_month_start="JAN",
                    money_services=True,
                    payment_services=True,
                    third_party_processor=True,
                    non_government_non_profit=True,
                    daily_discount=True,
                    non_bank_atm=True,
                    embassy=True,
                    high_inter_annual_trans_ngo=True,
                ),
                sales_rep_code="12345",
                additional_shareholders=[
                    Person(
                        name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        contact_info=ContactInfo(
                            address=Address(
                                street_name="Baker Street",
                                street_number="221",
                                line_two="Apt B",
                                line_three="48",
                                city="Atlanta",
                                county="Fulton",
                                post_code="30346",
                                country="USA",
                                state="USA_AL",
                                classification="BUSINESS_STREET_ADDRESS",
                                contact_name=Name(
                                    salutation="MR",
                                    first_name="John",
                                    middle_name="Lee",
                                    last_name="Doe",
                                ),
                                location_name="Baker Plaza",
                            ),
                            additional_addresses={
                                "key": Address(
                                    street_name="Baker Street",
                                    street_number="221",
                                    line_two="Apt B",
                                    line_three="48",
                                    city="Atlanta",
                                    county="Fulton",
                                    post_code="30346",
                                    country="USA",
                                    state="USA_AL",
                                    classification="BUSINESS_STREET_ADDRESS",
                                    contact_name=Name(
                                        salutation="MR",
                                        first_name="John",
                                        middle_name="Lee",
                                        last_name="Doe",
                                    ),
                                    location_name="Baker Plaza",
                                ),
                            },
                            phone=PhoneNumber(
                                intl_code="44",
                                area_code="111",
                                number="1231234",
                                extension="2",
                            ),
                            mobile=PhoneNumber(
                                intl_code="44",
                                area_code="111",
                                number="1231234",
                                extension="2",
                            ),
                            fax=PhoneNumber(
                                intl_code="44",
                                area_code="111",
                                number="1231234",
                                extension="2",
                            ),
                            email_address="contactname@email.com",
                        ),
                        dob=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        positions={
                            "key": True,
                        },
                        ownership_pct="90",
                        ids=[
                            Identification(
                                id_type="PASSPORT",
                                id_number="123456789",
                                expiry_date=DateComponents(
                                    year=1970,
                                    month="JAN",
                                    day=15,
                                ),
                                issue_date=DateComponents(
                                    year=1970,
                                    month="JAN",
                                    day=15,
                                ),
                                issuing_country="USA",
                                issuing_state="USA_AL",
                                id_name="id_name_example",
                                issuing_agency="issuing_agency_example",
                            ),
                        ],
                        title_type="ACCOUNTING_MANAGER",
                        title="Chief Technology Officer",
                        signing_personal_guarantee=True,
                        responsible_party=True,
                        related_party=True,
                        residing_country="GBR",
                        primary_nationality="GBR",
                        secondary_nationality="IRL",
                        documentary_info=DocumentaryInfo(
                            documentary=True,
                            documentary_verifier="SALES_TEAM",
                            documentary_issuer="USA",
                            documentary_type="DRIVER_LICENSE",
                            id_number="111111117",
                            issue_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            expiry_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issuing_state="USA_AL",
                            foreign_issuing_state="foreign_issuing_state_example",
                        ),
                        alternate_address_info=AlternateAddressInfo(
                            document_needed=True,
                            document_verified=True,
                            alternate_address_document_type="BANK_STATEMENT",
                            document_name="document_name_example",
                        ),
                        is_new_owner=True,
                        directional_ownership_type="DIRECT_OWNERSHIP",
                        signing_agreement=True,
                        us_person=True,
                    ),
                ],
                contact=Person(
                    name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    contact_info=ContactInfo(
                        address=Address(
                            street_name="Baker Street",
                            street_number="221",
                            line_two="Apt B",
                            line_three="48",
                            city="Atlanta",
                            county="Fulton",
                            post_code="30346",
                            country="USA",
                            state="USA_AL",
                            classification="BUSINESS_STREET_ADDRESS",
                            contact_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            location_name="Baker Plaza",
                        ),
                        additional_addresses={
                            "key": Address(
                                street_name="Baker Street",
                                street_number="221",
                                line_two="Apt B",
                                line_three="48",
                                city="Atlanta",
                                county="Fulton",
                                post_code="30346",
                                country="USA",
                                state="USA_AL",
                                classification="BUSINESS_STREET_ADDRESS",
                                contact_name=Name(
                                    salutation="MR",
                                    first_name="John",
                                    middle_name="Lee",
                                    last_name="Doe",
                                ),
                                location_name="Baker Plaza",
                            ),
                        },
                        phone=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        mobile=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        fax=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        email_address="contactname@email.com",
                    ),
                    dob=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    positions={
                        "key": True,
                    },
                    ownership_pct="90",
                    ids=[
                        Identification(
                            id_type="PASSPORT",
                            id_number="123456789",
                            expiry_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issue_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issuing_country="USA",
                            issuing_state="USA_AL",
                            id_name="id_name_example",
                            issuing_agency="issuing_agency_example",
                        ),
                    ],
                    title_type="ACCOUNTING_MANAGER",
                    title="Chief Technology Officer",
                    signing_personal_guarantee=True,
                    responsible_party=True,
                    related_party=True,
                    residing_country="GBR",
                    primary_nationality="GBR",
                    secondary_nationality="IRL",
                    documentary_info=DocumentaryInfo(
                        documentary=True,
                        documentary_verifier="SALES_TEAM",
                        documentary_issuer="USA",
                        documentary_type="DRIVER_LICENSE",
                        id_number="111111117",
                        issue_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        expiry_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        issuing_state="USA_AL",
                        foreign_issuing_state="foreign_issuing_state_example",
                    ),
                    alternate_address_info=AlternateAddressInfo(
                        document_needed=True,
                        document_verified=True,
                        alternate_address_document_type="BANK_STATEMENT",
                        document_name="document_name_example",
                    ),
                    is_new_owner=True,
                    directional_ownership_type="DIRECT_OWNERSHIP",
                    signing_agreement=True,
                    us_person=True,
                ),
                bank_accounts={
                    "key": BankingInfo(
                        account_name="John Doe",
                        bank_name="Wells Fargo",
                        urgent_payment=True,
                        funding_method="NETCREDIT",
                        account_number="20581687",
                        sort_code="121000248",
                        iban="GB48LOYD3037341",
                        swift_code="CPRTGB22",
                        bank_creditor_id="bank_creditor_id_example",
                        bank_direct=True,
                        country="GBR",
                        tape_id="14",
                        true_daily=True,
                        use_chain_account_number=True,
                    ),
                },
                card_pricing=CardPricing(
                    pricing_method="CLEAR_AND_SIMPLE",
                    pricing_category="RETAIL",
                    amex_accepting_info=AmexAcceptingInfo(
                        amex_monthly_card_sales=3553.0,
                        is_existing=True,
                        amex_mid="2101491576",
                    ),
                    payment_facilitator_info=PaymentFacilitatorInfo(
                        payment_facilitator_type="PAYMENT_FACILITATOR",
                        card_prefixes=[
                            CardPrefix(
                                card_type="VISA",
                                prefix="DE",
                            ),
                        ],
                    ),
                    card_charges=[
                        CardCharge(
                            card_type="VISA",
                            minimum_fee=0.03,
                            authorization_fee=3.14,
                            se_number="123456789",
                            service_type="PARTIAL_SERVICE",
                            card_funding="ELAVON",
                            pricing_tiers={
                                "key": PricingTier(
                                    discount_rate=2.0,
                                    discount_per_item=0.2,
                                ),
                            },
                        ),
                    ],
                    exception_charges=[
                        ExceptionCharge(
                            type="BUSINESS_CARDS",
                            discount_rate=1.0,
                            discount_per_item=0.1,
                        ),
                    ],
                    debit_pricing=DebitPricing(
                        pricing_method="INTERCHANGE_DIFFERENTIAL",
                        authorization_method="FIXED",
                        surcharge_amount=1.1,
                        surcharge_percent="0.1",
                        debit_network_charges=[
                            DebitNetworkCharge(
                                type="INTERLINK",
                                discount_rate=5.0,
                                discount_per_item=0.5,
                                per_auth=3.14,
                            ),
                        ],
                        pinless_setup=True,
                    ),
                ),
                fees=[
                    Fee(
                        type="JOI",
                        quantity=1,
                        amount=9.99,
                        frequency="ANNUAL",
                        start_month="JAN",
                    ),
                ],
                monetary_pricing_program="monetary_pricing_program_example",
                authenticate_pricing_program="47777",
                parent_entity="parent_entity_example",
                short_name="MS00EPNA",
                fraud_check_result=FraudCheckResult(
                    transaction_id="1100000000540130",
                    decision="PASS",
                ),
                site_survey=SiteSurvey(
                    site_survey_conducted=True,
                    location_type="SHOPPING_CENTRE",
                    site_address_same_as_dba=True,
                    location_environment="BUSINESS_DISTRICT",
                    vicinity_condition="WELL_KEPT",
                    location_square_meters="LTE_TO_250",
                    location_appearance="VERY_GOOD",
                    business_operating=True,
                    inventory_display_adequate=True,
                    inventory_consistent_with_business_type=True,
                    card_decals_visible=True,
                    card_decals_installed_at_visit=True,
                ),
                dynamic_currency_conversion=DynamicCurrencyConversion(
                    rebate_percent=0.5,
                    mark_up="ZERO",
                    currency_group="FIVE_USD_DCC_CURRENCIES",
                    registration_fee=2.0,
                ),
                billing_statement=BillingStatement(
                    type="SURCHARGE_TIERED",
                    media="DYNAMIC_MERCHANT_REPORTING",
                    address_type="BUSINESS",
                    email_address="applicantname@email.com",
                    frequency="DAILY",
                ),
                funding_statement=FundingStatement(
                    type="SURCHARGE_TIERED",
                    media="DYNAMIC_MERCHANT_REPORTING",
                    email_address="applicant@email.com",
                    frequency="DAILY",
                ),
                electronic_statement=ElectronicStatement(
                    type="SURCHARGE_TIERED",
                    media="DYNAMIC_MERCHANT_REPORTING",
                    email_address="applicant@email.com",
                    frequency="DAILY",
                ),
                vat_invoice_statement=VatInvoiceStatement(
                    type="SURCHARGE_TIERED",
                    media="DYNAMIC_MERCHANT_REPORTING",
                    address_type="BUSINESS",
                ),
                billing_method="NETCREDIT",
                referrer_name="PARTNER_BANK",
                referrer_reference_number="11",
                previous_processor="previous_processor_example",
                value_added_info=ValueAddedInfo(
                    value_adds={
                        "key": True,
                    },
                    ebt_info=EbtInfo(
                        se_number="123456789",
                        authorization_fee=0.03,
                    ),
                    ecs_info=EcsInfo(
                        processing_acceptance_type="POP_POS_IMAGE",
                        service_level_type="GUARANTEE_WITH_VERIFY",
                        annual_check_volume=100000.0,
                        average_check_amount=25.0,
                        max_check_amount=1000,
                        per_transaction=0.0,
                        discount_rate=0.0,
                        monthly_minimum=0.0,
                        per_return_fee=0.0,
                        nsf_service_processing_fee=0.0,
                        nsf_service_fee=0.0,
                        collection=True,
                        enquire_reporting=True,
                        service_provider_type="ENCIRCLE_DIRECT",
                    ),
                    acs_info=AcsInfo(
                        reporting_id="reporting_id_example",
                    ),
                    fanfare_info=FanfareInfo(
                        max_card_value="max_card_value_example",
                        package_type="STANDARD_GIFT_LOYALTY",
                        enrollment={
                            "key": EnrollmentInfo(
                                discount_rate=0.0,
                                discount_amount=0.0,
                            ),
                        },
                        loyalty={
                            "key": LoyaltyInfo(
                                visits=1,
                                amount_spent=22.0,
                                discount_rate=1.1,
                                discount_amount=5.0,
                            ),
                        },
                    ),
                    gsm_prepaid_type="EURONET_NO_PAYS",
                    surcharge_managed_by="surcharge_managed_by_example",
                    credit_surcharge_amt="credit_surcharge_amt_example",
                    efs3d_secure_info=Efs3dSecureInfo(
                        billing_per_item_fee=3.14,
                    ),
                    straight_send_info=StraightSendInfo(
                        per_transaction_fee=3.14,
                        percent_fee=3.14,
                    ),
                    on_demand_info=OnDemandInfo(
                        per_transaction_fee=3.14,
                        percent_fee=3.14,
                    ),
                    ocm_info=OcmInfo(
                        setup_type="Mid, Chain",
                        setup_fee=0.0,
                        monthly_fee=0.0,
                        number_of_users=1,
                    ),
                ),
                equipment_info=EquipmentInfo(
                    equipment_items=[
                        EquipmentItem(
                            code="310T3",
                            quantity=2,
                            pricing_items=[
                                EquipmentPricing(
                                    amount=200.0,
                                    purchase_type="EXCHANGE",
                                    lease_term=1,
                                    vendor_code=1,
                                    vendor_plan="vendor_plan_example",
                                    start_month="JAN",
                                    start_year="2010",
                                ),
                            ],
                            item_settings=ItemSettings(
                                security_level="BASIC",
                                semi_integrated=True,
                                connection_type="STANDARD_IP",
                                close_method="MANUAL",
                                capture_method="HOST",
                                qir_vendor="qir_vendor_example",
                                services={
                                    "key": True,
                                },
                                options=[
                                    EquipmentOption(
                                        integrator_code="integrator_code_example",
                                        ciers_number="ciers_number_example",
                                        serial_number="serial_number_example",
                                        model_number="model_number_example",
                                        ecr_type="SMARTLINK",
                                        ecr_mode="LITE_TOUCH",
                                        print_via_ecr=True,
                                        ecr_integrator="ALMAR",
                                        ecr_cable_type="NONE",
                                        epg_integration_type="REMOTE",
                                        bax_number="bax_number_example",
                                        bax_effective_date=DateComponents(
                                            year=1970,
                                            month="JAN",
                                            day=15,
                                        ),
                                    ),
                                ],
                                bundled_thresh_hold=1,
                                service_pricing_code="CORE",
                                terminal_type="INTERNET",
                                ingenico_pay_table=True,
                                deploy_type="DEPLOY",
                            ),
                            exception_items=[
                                ExceptionItem(
                                    type="type_example",
                                    discount_rate=3.14,
                                    discount_per_item=3.14,
                                ),
                            ],
                            service_fee=3.14,
                            trx_free_month=1,
                            future_effective_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                        ),
                    ],
                    terminal_services=[
                        TerminalService(
                            type="QUICK_CLOSE",
                            service_specifics="service_specifics_example",
                        ),
                    ],
                    training_type="TRAINING",
                    shipping_method="NEXT_DAY",
                    network="ELAVON",
                    fusebox_info=FuseboxInfo(
                        simplify_quantity=1,
                        direct_quantity=1,
                        simplify_location="simplify_location_example",
                        direct_to_fusebox_location="direct_to_fusebox_location_example",
                    ),
                    anticipated_start_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                ),
                branch_number="111",
                branch_code="1234",
                self_boarded_external=True,
                employee_number="11222",
                rep_referral_number="321",
                promotional_code="00001",
                chain_info=ChainInfo(
                    chain_number="chain_number_example",
                    chain_name="chain_name_example",
                    send_statement_to_address="BUSINESS",
                    statement_media="DYNAMIC_MERCHANT_REPORTING",
                    address=Address(
                        street_name="Baker Street",
                        street_number="221",
                        line_two="Apt B",
                        line_three="48",
                        city="Atlanta",
                        county="Fulton",
                        post_code="30346",
                        country="USA",
                        state="USA_AL",
                        classification="BUSINESS_STREET_ADDRESS",
                        contact_name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        location_name="Baker Plaza",
                    ),
                    chain_level_billing=True,
                    bank_accounts={
                        "key": BankingInfo(
                            account_name="John Doe",
                            bank_name="Wells Fargo",
                            urgent_payment=True,
                            funding_method="NETCREDIT",
                            account_number="20581687",
                            sort_code="121000248",
                            iban="GB48LOYD3037341",
                            swift_code="CPRTGB22",
                            bank_creditor_id="bank_creditor_id_example",
                            bank_direct=True,
                            country="GBR",
                            tape_id="14",
                            true_daily=True,
                            use_chain_account_number=True,
                        ),
                    },
                ),
                distributions={
                    "key": DistributionInfo(
                        method="MAILING",
                        address_type="BUSINESS",
                        email_address="applicant@email.com",
                    ),
                },
                additional_location_info=AdditionalLocationInfo(
                    central_mid="8024999222",
                    central_legal_name="Elavon",
                    central_tax_id="787421357",
                ),
                signed_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                signed_type="WET",
                intermediary_owner_info=IntermediaryOwnerInfo(
                    intermediary_owners=[
                        IntermediaryOwner(
                            ownership_pct="90",
                            business_name="ACME",
                            owner_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            phone=PhoneNumber(
                                intl_code="44",
                                area_code="111",
                                number="1231234",
                                extension="2",
                            ),
                            email_address="email_address_example",
                            address=Address(
                                street_name="Baker Street",
                                street_number="221",
                                line_two="Apt B",
                                line_three="48",
                                city="Atlanta",
                                county="Fulton",
                                post_code="30346",
                                country="USA",
                                state="USA_AL",
                                classification="BUSINESS_STREET_ADDRESS",
                                contact_name=Name(
                                    salutation="MR",
                                    first_name="John",
                                    middle_name="Lee",
                                    last_name="Doe",
                                ),
                                location_name="Baker Plaza",
                            ),
                        ),
                    ],
                    additional_intermediate_owners=True,
                ),
                revenue_share_info=RevenueShareInfo(
                    secondary_sales_person="12345",
                    split_percentage="50",
                ),
                elavon_contract="UK",
                internal_use_info=InternalUseInfo(
                    field_auto_info=FieldAutoInfo(
                        requested=True,
                        applied=True,
                        monitored=True,
                        values_modified=True,
                        field_auto_reference_id="field_auto_reference_id_example",
                    ),
                    sales_rep_info=SalesRepInfo(
                        sales_rep_code="12345",
                        name="name_example",
                        email="repname@email.com",
                        submitted=True,
                    ),
                    tin_applied_to_all=True,
                    ip_address="ip_address_example",
                ),
                eframe_info=EframeInfo(
                    scheme_selection="scheme_selection_example",
                    pos_contract=True,
                    is_girocard=True,
                ),
                partner_info=PartnerInfo(
                    partner_name="partner_name_example",
                    associate_id="associate_id_example",
                    book_of_business="book_of_business_example",
                    correlation_id="correlation_id_example",
                    partner_source="partner_source_example",
                    merchant_user_id="merchant_user_id_example",
                    session_id="session_id_example",
                ),
                alternative_payment_methods=[
                    ApmAcquirer(
                        acquirer_code="acquirer_code_example",
                        acquirer_types=[
                            ApmAcquirerType(
                                type_code="type_code_example",
                                per_item_amount="per_item_amount_example",
                                rate_percentage="rate_percentage_example",
                                pricing_tiers=[
                                    ApmPricingTier(
                                        combining_code="combining_code_example",
                                        per_item_amount="per_item_amount_example",
                                        rate_percentage="rate_percentage_example",
                                        description="description_example",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            language="language_example",
            agreement_id="agreement_id_example",
            is_grouped_application=True,
            wet_signed=True,
            card_volume=CardVolume(
                visa_percentage="15.6",
                master_card_percentage="12.3",
                amex_percentage="4.5",
                amex_average_transaction="10.1",
                interac_average_transaction="23.4",
            ),
            vendor_info=ProviderInfo(
                representative_name="Alex Smith",
                representative_email="asmith@email.com",
                representative_sales_code="12345",
                representative_contact_number=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
            ),
            acting_intermediary_info=ActingIntermediaryInfo(
                acting_intermediary_name="acting_intermediary_name_example",
                acting_intermediary_type="QUALIFIED_INTERMEDIARY",
            ),
            bank_account_details_map={
                "key": BankAccountAdditionalInfo(
                    bank_name="bank_name_example",
                    bank_branch="bank_branch_example",
                    direct_debit_authorized=True,
                ),
            },
            is_tax_exempt_equipment=True,
            talech_egift_only=True,
            displayed_currency="displayed_currency_example",
            additional_description_info=AdditionalDescriptionInfo(
                previous_processor_description="Bank of America",
                monetary_pricing_program_description="MIF Unblended",
                referrer_reference_description="referrer_reference_description_example",
                notes="notes_example",
            ),
            additional_value_added_service_info=ValueAddedServices(
                ecs=ElectronicCheckService(
                    reporting_fee=3.14,
                    reporting_num_users="reporting_num_users_example",
                    ach_check_questions=AchCheckQuestions(
                        payment_acceptance_type="payment_acceptance_type_example",
                        prior_acceptance_authorization=True,
                        customer_identification=True,
                        ach_customer_type="EXISTING",
                        maintain_and_disclose_cancel=True,
                        ensure_accurate_transaction_info=True,
                    ),
                ),
                fanfare=Fanfare(
                    setup_fee=1.1,
                    monthly_fee=0.06,
                    annual_fee=1.6,
                    custom_card_upgrade_fee=0.02,
                    included_cards=FanfareCardSplits(
                        promotional="promotional_example",
                        loyalty="loyalty_example",
                        gift="gift_example",
                    ),
                    additional_cards_type="FF_STANDARD",
                    additional_cards=FanfareCardSplits(
                        promotional="promotional_example",
                        loyalty="loyalty_example",
                        gift="gift_example",
                    ),
                    additional_card_price=3.14,
                    program_checkup=3.14,
                    card_style="card_style_example",
                    justification_type="LEFT",
                    card_is_text=True,
                    card_text="card_text_example",
                    text_case_type="TITLE_CASE",
                    text_color="text_color_example",
                    text_font="text_font_example",
                ),
            ),
            additional_business_info=AdditionalBusinessInfo(
                ownership_years_over_range="3",
                is_max_establishment_year=True,
                has_government_incentive=True,
            ),
            funding_type="STANDARD",
            integrator_solution_info=IntegratorSolutionInfo(
                health_care_eligibility_selection_map={
                    "key": HealthCareEligibilityInfo(
                        monthly_fee=0.0,
                        npi_numbers=[
                            "npi_numbers_example",
                        ],
                    ),
                },
                payments=Payments(
                    pms_vendor_pas="pms_vendor_pas_example",
                    number_of_providers="1",
                    sales_rep_phone_number="sales_rep_phone_number_example",
                    integrator_notes="1111111111",
                    has_payment_plans=True,
                ),
                has_ecs_only=True,
                sku="310T3",
            ),
            additional_lease_info=AdditionalLeaseInfo(
                lease_details_map={
                    "key": LeaseDetails(
                        alternate_price=3.14,
                        pricing_plan="pricing_plan_example",
                    ),
                },
            ),
            marketing_data_consent_map={
                "key": True,
            },
            additional_site_survey_info=AdditionalSiteSurveyInfo(
                incomplete_survey_reason_type="NOT_OPEN",
                site_survey_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                site_survey_conducted_by="site_survey_conducted_by_example",
                description_of_no_site_survey="description_of_no_site_survey_example",
            ),
            kyc_quiz_status_map={
                "KYC_RESULT_FAILED_QUIZ": "KYC_RESULT_FAILED_QUIZ",
            },
            var_other_details=VarOtherDetails(
                var_type="VENDOR_DISTRIBUTED",
                vendor="vendor_example",
                product="product_example",
                version="version_example",
            ),
            additional_card_pricing_info=AdditionalCardPricingInfo(
                minimum_card_fee=0.0,
                clear_and_simple_type="clear_and_simple_type_example",
                c4_pricing_type="c4_pricing_type_example",
                high_risk_cost_additional_loading="high_risk_cost_additional_loading_example",
            ),
            sales_office_contact=SalesOfficeContact(
                address=Address(
                    street_name="Baker Street",
                    street_number="221",
                    line_two="Apt B",
                    line_three="48",
                    city="Atlanta",
                    county="Fulton",
                    post_code="30346",
                    country="USA",
                    state="USA_AL",
                    classification="BUSINESS_STREET_ADDRESS",
                    contact_name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    location_name="Baker Plaza",
                ),
                phone=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
            ),
            sales_person_contact=SalesPersonContact(
                name=Name(
                    salutation="MR",
                    first_name="John",
                    middle_name="Lee",
                    last_name="Doe",
                ),
                phone=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                email_address="email_address_example",
            ),
            additional_auth_pricing_program_info=AdditionalAuthPricingProgramInfo(
                description="description_example",
                fee=5.0,
                auth_amount=10.0,
            ),
            applicant_email="applicant_email_example",
            partner_document_data={
                "key": {
                    "key": "key_example",
                },
            },
            application_id=1,
        ),
    ) # UpdateDocumentPacketRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update Document Packet
        api_response = api_instance.update_document_packet(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->update_document_packet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateDocumentPacketRequest**](UpdateDocumentPacketRequest.md)|  |

### Return type

[**UpdateDocumentPacketResponse**](UpdateDocumentPacketResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Update Document Packet Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document_packet_data**
> UpdateDocumentPacketDataResponse update_document_packet_data(body)

Update document packet

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.update_document_packet_data_request import UpdateDocumentPacketDataRequest
from elavon.model.update_document_packet_data_response import UpdateDocumentPacketDataResponse
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    body = UpdateDocumentPacketDataRequest(
        signers=[
            Signer(
                signer_id="signer_id_example",
                signer=Name(
                    salutation="MR",
                    first_name="John",
                    middle_name="Lee",
                    last_name="Doe",
                ),
                email_address="email_address_example",
                principal=True,
                signing_complete_url="signing_complete_url_example",
                signing_decline_url="signing_decline_url_example",
                signing_expired_url="signing_expired_url_example",
                language="language_example",
                opt_in_out1=True,
                opt_in_out2=True,
                opt_in_out3=True,
            ),
        ],
        document_packet_id="document_packet_id_example",
        document_packet_data=DocumentPacketData(
            scarecrow_application=ScarecrowApplication(
                client_id="IDNA",
                client_group_number="860",
                unique_id="AcmeCorp1572566399123",
                banker_id="123",
                banker_partner_id="123",
                country="USA",
                principal=Person(
                    name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    contact_info=ContactInfo(
                        address=Address(
                            street_name="Baker Street",
                            street_number="221",
                            line_two="Apt B",
                            line_three="48",
                            city="Atlanta",
                            county="Fulton",
                            post_code="30346",
                            country="USA",
                            state="USA_AL",
                            classification="BUSINESS_STREET_ADDRESS",
                            contact_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            location_name="Baker Plaza",
                        ),
                        additional_addresses={
                            "key": Address(
                                street_name="Baker Street",
                                street_number="221",
                                line_two="Apt B",
                                line_three="48",
                                city="Atlanta",
                                county="Fulton",
                                post_code="30346",
                                country="USA",
                                state="USA_AL",
                                classification="BUSINESS_STREET_ADDRESS",
                                contact_name=Name(
                                    salutation="MR",
                                    first_name="John",
                                    middle_name="Lee",
                                    last_name="Doe",
                                ),
                                location_name="Baker Plaza",
                            ),
                        },
                        phone=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        mobile=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        fax=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        email_address="contactname@email.com",
                    ),
                    dob=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    positions={
                        "key": True,
                    },
                    ownership_pct="90",
                    ids=[
                        Identification(
                            id_type="PASSPORT",
                            id_number="123456789",
                            expiry_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issue_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issuing_country="USA",
                            issuing_state="USA_AL",
                            id_name="id_name_example",
                            issuing_agency="issuing_agency_example",
                        ),
                    ],
                    title_type="ACCOUNTING_MANAGER",
                    title="Chief Technology Officer",
                    signing_personal_guarantee=True,
                    responsible_party=True,
                    related_party=True,
                    residing_country="GBR",
                    primary_nationality="GBR",
                    secondary_nationality="IRL",
                    documentary_info=DocumentaryInfo(
                        documentary=True,
                        documentary_verifier="SALES_TEAM",
                        documentary_issuer="USA",
                        documentary_type="DRIVER_LICENSE",
                        id_number="111111117",
                        issue_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        expiry_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        issuing_state="USA_AL",
                        foreign_issuing_state="foreign_issuing_state_example",
                    ),
                    alternate_address_info=AlternateAddressInfo(
                        document_needed=True,
                        document_verified=True,
                        alternate_address_document_type="BANK_STATEMENT",
                        document_name="document_name_example",
                    ),
                    is_new_owner=True,
                    directional_ownership_type="DIRECT_OWNERSHIP",
                    signing_agreement=True,
                    us_person=True,
                ),
                business_info=BusinessInfo(
                    dba_name="Grimm's Bookstore",
                    dba_name_extended="Grimm's Fairytales and Other Stories Bookstore",
                    business_address=Address(
                        street_name="Baker Street",
                        street_number="221",
                        line_two="Apt B",
                        line_three="48",
                        city="Atlanta",
                        county="Fulton",
                        post_code="30346",
                        country="USA",
                        state="USA_AL",
                        classification="BUSINESS_STREET_ADDRESS",
                        contact_name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        location_name="Baker Plaza",
                    ),
                    legal_name="Barkers Dog Bakery",
                    legal_name_extended="Baking Better Biscuits for Your Favorite Barkers Dog Bakery LLC",
                    legal_name_marked=[
                        "legal_name_marked_example",
                    ],
                    additional_addresses={
                        "key": Address(
                            street_name="Baker Street",
                            street_number="221",
                            line_two="Apt B",
                            line_three="48",
                            city="Atlanta",
                            county="Fulton",
                            post_code="30346",
                            country="USA",
                            state="USA_AL",
                            classification="BUSINESS_STREET_ADDRESS",
                            contact_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            location_name="Baker Plaza",
                        ),
                    },
                    ownership_type="SOLE_TRADER",
                    registration_number="1234567",
                    tax_id="787421357",
                    tax_id_type="FEDERAL_TAX_ID",
                    vat_info=VatInfo(
                        number_option="VAT_NBR",
                        number56_b="123456789",
                        expiry_date56_b=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        tax_number_type="CORPORATE_TAX_NUMBER",
                        tax_number="tax_number_example",
                    ),
                    tax_form_type="W9",
                    tax_class_type="CORPORATION",
                    customer_membership_number="111222",
                    product_description="Bakeries",
                    mcc_code="7399E",
                    establishment_year="2005",
                    current_ownership_years="3",
                    current_ownership_months="6",
                    government_owned_entity=True,
                    communication_language="en",
                    pos_language="en",
                    store_number="123456789",
                    association_codes=[
                        "12345",
                    ],
                    opt_out=True,
                    sign_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    pci_info=PCIInfo(
                        pci_program_level="ONE",
                        pci_service_type="BASIC",
                        pci_contact_first_name="pci_contact_first_name_example",
                        pci_contact_last_name="pci_contact_last_name_example",
                        pci_contact_email_address="pci_contact_email_address_example",
                        pci_contact_phone=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        pci_groups=[
                            "PCI_PROGRAM_EXCLUSION",
                        ],
                    ),
                    employer_id="1234567",
                    country_of_origin="USA",
                    exemption_type="ADDITIONAL_LOCATION",
                    owner_exemption_type="BANK_ADVISED_POOLED",
                    number_of_partners="ONE",
                    relationship_mgr_code="1234567",
                    country_of_primary_operation="USA",
                    bearer_shares=True,
                    legal_status="CERTIFIED_INCORPORATION_ARTICLES",
                    verifications={
                        "key": VerificationInfo(
                            documentary=True,
                            issuing_country="USA",
                            issuing_state="USA_AL",
                            site_person_met="John Smith",
                            site_visit_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            id_number="111111117",
                            issue_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            expiry_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            document_type="CERTIFIED_INCORPORATION_ARTICLES",
                        ),
                    },
                    industry_class="LODGING",
                    no_plates=True,
                    agent_number="1223334",
                    location_mid_range="NORDIC",
                    hemp_grower_info=HempGrowerInfo(
                        operations_description="operations_description_example",
                        is_licensed=True,
                        license_expiration_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        additional_mrb_activity=True,
                        cannabis_revenue_percentage_range="NONE",
                    ),
                    credit_decision_info=CreditDecisionInfo(
                        credit_decision_flag=True,
                        credit_decision_id="credit_decision_id_example",
                    ),
                ),
                financial_info=FinancialInfo(
                    avg_sale_amount="125",
                    monthly_card_sales="1000",
                    annual_card_sales="12000",
                    annual_revenue="240000",
                    highest_ticket_amount="1000",
                    highest_ticket_frequency=1,
                    funding_currency="USD",
                    card_present_acceptance_percent="100",
                    internet_acceptance_percent="0",
                    moto_acceptance_percent="0",
                    business_email_address="business_email_address_example",
                    business_website_url="business@email.com",
                    customer_service_phone=PhoneNumber(
                        intl_code="44",
                        area_code="111",
                        number="1231234",
                        extension="2",
                    ),
                    not_present_delay_days=0,
                    deposit_frequency="0",
                    deposit_size_percent="1",
                    deposit_balance_days="1",
                    deposit_fulfillment_days="1",
                    full_payment_percent="1",
                    full_payment_fulfillment="1",
                    utilize_cvv2=True,
                    recurring_transactions=True,
                    contract_term_type="ZERO_MONTH",
                    months_closed=[
                        "JAN",
                    ],
                    monetary_billing_method="CARD_DISCOUNT",
                    authorization_included=True,
                    annual_fee_month_start="JAN",
                    money_services=True,
                    payment_services=True,
                    third_party_processor=True,
                    non_government_non_profit=True,
                    daily_discount=True,
                    non_bank_atm=True,
                    embassy=True,
                    high_inter_annual_trans_ngo=True,
                ),
                sales_rep_code="12345",
                additional_shareholders=[
                    Person(
                        name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        contact_info=ContactInfo(
                            address=Address(
                                street_name="Baker Street",
                                street_number="221",
                                line_two="Apt B",
                                line_three="48",
                                city="Atlanta",
                                county="Fulton",
                                post_code="30346",
                                country="USA",
                                state="USA_AL",
                                classification="BUSINESS_STREET_ADDRESS",
                                contact_name=Name(
                                    salutation="MR",
                                    first_name="John",
                                    middle_name="Lee",
                                    last_name="Doe",
                                ),
                                location_name="Baker Plaza",
                            ),
                            additional_addresses={
                                "key": Address(
                                    street_name="Baker Street",
                                    street_number="221",
                                    line_two="Apt B",
                                    line_three="48",
                                    city="Atlanta",
                                    county="Fulton",
                                    post_code="30346",
                                    country="USA",
                                    state="USA_AL",
                                    classification="BUSINESS_STREET_ADDRESS",
                                    contact_name=Name(
                                        salutation="MR",
                                        first_name="John",
                                        middle_name="Lee",
                                        last_name="Doe",
                                    ),
                                    location_name="Baker Plaza",
                                ),
                            },
                            phone=PhoneNumber(
                                intl_code="44",
                                area_code="111",
                                number="1231234",
                                extension="2",
                            ),
                            mobile=PhoneNumber(
                                intl_code="44",
                                area_code="111",
                                number="1231234",
                                extension="2",
                            ),
                            fax=PhoneNumber(
                                intl_code="44",
                                area_code="111",
                                number="1231234",
                                extension="2",
                            ),
                            email_address="contactname@email.com",
                        ),
                        dob=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        positions={
                            "key": True,
                        },
                        ownership_pct="90",
                        ids=[
                            Identification(
                                id_type="PASSPORT",
                                id_number="123456789",
                                expiry_date=DateComponents(
                                    year=1970,
                                    month="JAN",
                                    day=15,
                                ),
                                issue_date=DateComponents(
                                    year=1970,
                                    month="JAN",
                                    day=15,
                                ),
                                issuing_country="USA",
                                issuing_state="USA_AL",
                                id_name="id_name_example",
                                issuing_agency="issuing_agency_example",
                            ),
                        ],
                        title_type="ACCOUNTING_MANAGER",
                        title="Chief Technology Officer",
                        signing_personal_guarantee=True,
                        responsible_party=True,
                        related_party=True,
                        residing_country="GBR",
                        primary_nationality="GBR",
                        secondary_nationality="IRL",
                        documentary_info=DocumentaryInfo(
                            documentary=True,
                            documentary_verifier="SALES_TEAM",
                            documentary_issuer="USA",
                            documentary_type="DRIVER_LICENSE",
                            id_number="111111117",
                            issue_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            expiry_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issuing_state="USA_AL",
                            foreign_issuing_state="foreign_issuing_state_example",
                        ),
                        alternate_address_info=AlternateAddressInfo(
                            document_needed=True,
                            document_verified=True,
                            alternate_address_document_type="BANK_STATEMENT",
                            document_name="document_name_example",
                        ),
                        is_new_owner=True,
                        directional_ownership_type="DIRECT_OWNERSHIP",
                        signing_agreement=True,
                        us_person=True,
                    ),
                ],
                contact=Person(
                    name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    contact_info=ContactInfo(
                        address=Address(
                            street_name="Baker Street",
                            street_number="221",
                            line_two="Apt B",
                            line_three="48",
                            city="Atlanta",
                            county="Fulton",
                            post_code="30346",
                            country="USA",
                            state="USA_AL",
                            classification="BUSINESS_STREET_ADDRESS",
                            contact_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            location_name="Baker Plaza",
                        ),
                        additional_addresses={
                            "key": Address(
                                street_name="Baker Street",
                                street_number="221",
                                line_two="Apt B",
                                line_three="48",
                                city="Atlanta",
                                county="Fulton",
                                post_code="30346",
                                country="USA",
                                state="USA_AL",
                                classification="BUSINESS_STREET_ADDRESS",
                                contact_name=Name(
                                    salutation="MR",
                                    first_name="John",
                                    middle_name="Lee",
                                    last_name="Doe",
                                ),
                                location_name="Baker Plaza",
                            ),
                        },
                        phone=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        mobile=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        fax=PhoneNumber(
                            intl_code="44",
                            area_code="111",
                            number="1231234",
                            extension="2",
                        ),
                        email_address="contactname@email.com",
                    ),
                    dob=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                    positions={
                        "key": True,
                    },
                    ownership_pct="90",
                    ids=[
                        Identification(
                            id_type="PASSPORT",
                            id_number="123456789",
                            expiry_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issue_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                            issuing_country="USA",
                            issuing_state="USA_AL",
                            id_name="id_name_example",
                            issuing_agency="issuing_agency_example",
                        ),
                    ],
                    title_type="ACCOUNTING_MANAGER",
                    title="Chief Technology Officer",
                    signing_personal_guarantee=True,
                    responsible_party=True,
                    related_party=True,
                    residing_country="GBR",
                    primary_nationality="GBR",
                    secondary_nationality="IRL",
                    documentary_info=DocumentaryInfo(
                        documentary=True,
                        documentary_verifier="SALES_TEAM",
                        documentary_issuer="USA",
                        documentary_type="DRIVER_LICENSE",
                        id_number="111111117",
                        issue_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        expiry_date=DateComponents(
                            year=1970,
                            month="JAN",
                            day=15,
                        ),
                        issuing_state="USA_AL",
                        foreign_issuing_state="foreign_issuing_state_example",
                    ),
                    alternate_address_info=AlternateAddressInfo(
                        document_needed=True,
                        document_verified=True,
                        alternate_address_document_type="BANK_STATEMENT",
                        document_name="document_name_example",
                    ),
                    is_new_owner=True,
                    directional_ownership_type="DIRECT_OWNERSHIP",
                    signing_agreement=True,
                    us_person=True,
                ),
                bank_accounts={
                    "key": BankingInfo(
                        account_name="John Doe",
                        bank_name="Wells Fargo",
                        urgent_payment=True,
                        funding_method="NETCREDIT",
                        account_number="20581687",
                        sort_code="121000248",
                        iban="GB48LOYD3037341",
                        swift_code="CPRTGB22",
                        bank_creditor_id="bank_creditor_id_example",
                        bank_direct=True,
                        country="GBR",
                        tape_id="14",
                        true_daily=True,
                        use_chain_account_number=True,
                    ),
                },
                card_pricing=CardPricing(
                    pricing_method="CLEAR_AND_SIMPLE",
                    pricing_category="RETAIL",
                    amex_accepting_info=AmexAcceptingInfo(
                        amex_monthly_card_sales=3553.0,
                        is_existing=True,
                        amex_mid="2101491576",
                    ),
                    payment_facilitator_info=PaymentFacilitatorInfo(
                        payment_facilitator_type="PAYMENT_FACILITATOR",
                        card_prefixes=[
                            CardPrefix(
                                card_type="VISA",
                                prefix="DE",
                            ),
                        ],
                    ),
                    card_charges=[
                        CardCharge(
                            card_type="VISA",
                            minimum_fee=0.03,
                            authorization_fee=3.14,
                            se_number="123456789",
                            service_type="PARTIAL_SERVICE",
                            card_funding="ELAVON",
                            pricing_tiers={
                                "key": PricingTier(
                                    discount_rate=2.0,
                                    discount_per_item=0.2,
                                ),
                            },
                        ),
                    ],
                    exception_charges=[
                        ExceptionCharge(
                            type="BUSINESS_CARDS",
                            discount_rate=1.0,
                            discount_per_item=0.1,
                        ),
                    ],
                    debit_pricing=DebitPricing(
                        pricing_method="INTERCHANGE_DIFFERENTIAL",
                        authorization_method="FIXED",
                        surcharge_amount=1.1,
                        surcharge_percent="0.1",
                        debit_network_charges=[
                            DebitNetworkCharge(
                                type="INTERLINK",
                                discount_rate=5.0,
                                discount_per_item=0.5,
                                per_auth=3.14,
                            ),
                        ],
                        pinless_setup=True,
                    ),
                ),
                fees=[
                    Fee(
                        type="JOI",
                        quantity=1,
                        amount=9.99,
                        frequency="ANNUAL",
                        start_month="JAN",
                    ),
                ],
                monetary_pricing_program="monetary_pricing_program_example",
                authenticate_pricing_program="47777",
                parent_entity="parent_entity_example",
                short_name="MS00EPNA",
                fraud_check_result=FraudCheckResult(
                    transaction_id="1100000000540130",
                    decision="PASS",
                ),
                site_survey=SiteSurvey(
                    site_survey_conducted=True,
                    location_type="SHOPPING_CENTRE",
                    site_address_same_as_dba=True,
                    location_environment="BUSINESS_DISTRICT",
                    vicinity_condition="WELL_KEPT",
                    location_square_meters="LTE_TO_250",
                    location_appearance="VERY_GOOD",
                    business_operating=True,
                    inventory_display_adequate=True,
                    inventory_consistent_with_business_type=True,
                    card_decals_visible=True,
                    card_decals_installed_at_visit=True,
                ),
                dynamic_currency_conversion=DynamicCurrencyConversion(
                    rebate_percent=0.5,
                    mark_up="ZERO",
                    currency_group="FIVE_USD_DCC_CURRENCIES",
                    registration_fee=2.0,
                ),
                billing_statement=BillingStatement(
                    type="SURCHARGE_TIERED",
                    media="DYNAMIC_MERCHANT_REPORTING",
                    address_type="BUSINESS",
                    email_address="applicantname@email.com",
                    frequency="DAILY",
                ),
                funding_statement=FundingStatement(
                    type="SURCHARGE_TIERED",
                    media="DYNAMIC_MERCHANT_REPORTING",
                    email_address="applicant@email.com",
                    frequency="DAILY",
                ),
                electronic_statement=ElectronicStatement(
                    type="SURCHARGE_TIERED",
                    media="DYNAMIC_MERCHANT_REPORTING",
                    email_address="applicant@email.com",
                    frequency="DAILY",
                ),
                vat_invoice_statement=VatInvoiceStatement(
                    type="SURCHARGE_TIERED",
                    media="DYNAMIC_MERCHANT_REPORTING",
                    address_type="BUSINESS",
                ),
                billing_method="NETCREDIT",
                referrer_name="PARTNER_BANK",
                referrer_reference_number="11",
                previous_processor="previous_processor_example",
                value_added_info=ValueAddedInfo(
                    value_adds={
                        "key": True,
                    },
                    ebt_info=EbtInfo(
                        se_number="123456789",
                        authorization_fee=0.03,
                    ),
                    ecs_info=EcsInfo(
                        processing_acceptance_type="POP_POS_IMAGE",
                        service_level_type="GUARANTEE_WITH_VERIFY",
                        annual_check_volume=100000.0,
                        average_check_amount=25.0,
                        max_check_amount=1000,
                        per_transaction=0.0,
                        discount_rate=0.0,
                        monthly_minimum=0.0,
                        per_return_fee=0.0,
                        nsf_service_processing_fee=0.0,
                        nsf_service_fee=0.0,
                        collection=True,
                        enquire_reporting=True,
                        service_provider_type="ENCIRCLE_DIRECT",
                    ),
                    acs_info=AcsInfo(
                        reporting_id="reporting_id_example",
                    ),
                    fanfare_info=FanfareInfo(
                        max_card_value="max_card_value_example",
                        package_type="STANDARD_GIFT_LOYALTY",
                        enrollment={
                            "key": EnrollmentInfo(
                                discount_rate=0.0,
                                discount_amount=0.0,
                            ),
                        },
                        loyalty={
                            "key": LoyaltyInfo(
                                visits=1,
                                amount_spent=22.0,
                                discount_rate=1.1,
                                discount_amount=5.0,
                            ),
                        },
                    ),
                    gsm_prepaid_type="EURONET_NO_PAYS",
                    surcharge_managed_by="surcharge_managed_by_example",
                    credit_surcharge_amt="credit_surcharge_amt_example",
                    efs3d_secure_info=Efs3dSecureInfo(
                        billing_per_item_fee=3.14,
                    ),
                    straight_send_info=StraightSendInfo(
                        per_transaction_fee=3.14,
                        percent_fee=3.14,
                    ),
                    on_demand_info=OnDemandInfo(
                        per_transaction_fee=3.14,
                        percent_fee=3.14,
                    ),
                    ocm_info=OcmInfo(
                        setup_type="Mid, Chain",
                        setup_fee=0.0,
                        monthly_fee=0.0,
                        number_of_users=1,
                    ),
                ),
                equipment_info=EquipmentInfo(
                    equipment_items=[
                        EquipmentItem(
                            code="310T3",
                            quantity=2,
                            pricing_items=[
                                EquipmentPricing(
                                    amount=200.0,
                                    purchase_type="EXCHANGE",
                                    lease_term=1,
                                    vendor_code=1,
                                    vendor_plan="vendor_plan_example",
                                    start_month="JAN",
                                    start_year="2010",
                                ),
                            ],
                            item_settings=ItemSettings(
                                security_level="BASIC",
                                semi_integrated=True,
                                connection_type="STANDARD_IP",
                                close_method="MANUAL",
                                capture_method="HOST",
                                qir_vendor="qir_vendor_example",
                                services={
                                    "key": True,
                                },
                                options=[
                                    EquipmentOption(
                                        integrator_code="integrator_code_example",
                                        ciers_number="ciers_number_example",
                                        serial_number="serial_number_example",
                                        model_number="model_number_example",
                                        ecr_type="SMARTLINK",
                                        ecr_mode="LITE_TOUCH",
                                        print_via_ecr=True,
                                        ecr_integrator="ALMAR",
                                        ecr_cable_type="NONE",
                                        epg_integration_type="REMOTE",
                                        bax_number="bax_number_example",
                                        bax_effective_date=DateComponents(
                                            year=1970,
                                            month="JAN",
                                            day=15,
                                        ),
                                    ),
                                ],
                                bundled_thresh_hold=1,
                                service_pricing_code="CORE",
                                terminal_type="INTERNET",
                                ingenico_pay_table=True,
                                deploy_type="DEPLOY",
                            ),
                            exception_items=[
                                ExceptionItem(
                                    type="type_example",
                                    discount_rate=3.14,
                                    discount_per_item=3.14,
                                ),
                            ],
                            service_fee=3.14,
                            trx_free_month=1,
                            future_effective_date=DateComponents(
                                year=1970,
                                month="JAN",
                                day=15,
                            ),
                        ),
                    ],
                    terminal_services=[
                        TerminalService(
                            type="QUICK_CLOSE",
                            service_specifics="service_specifics_example",
                        ),
                    ],
                    training_type="TRAINING",
                    shipping_method="NEXT_DAY",
                    network="ELAVON",
                    fusebox_info=FuseboxInfo(
                        simplify_quantity=1,
                        direct_quantity=1,
                        simplify_location="simplify_location_example",
                        direct_to_fusebox_location="direct_to_fusebox_location_example",
                    ),
                    anticipated_start_date=DateComponents(
                        year=1970,
                        month="JAN",
                        day=15,
                    ),
                ),
                branch_number="111",
                branch_code="1234",
                self_boarded_external=True,
                employee_number="11222",
                rep_referral_number="321",
                promotional_code="00001",
                chain_info=ChainInfo(
                    chain_number="chain_number_example",
                    chain_name="chain_name_example",
                    send_statement_to_address="BUSINESS",
                    statement_media="DYNAMIC_MERCHANT_REPORTING",
                    address=Address(
                        street_name="Baker Street",
                        street_number="221",
                        line_two="Apt B",
                        line_three="48",
                        city="Atlanta",
                        county="Fulton",
                        post_code="30346",
                        country="USA",
                        state="USA_AL",
                        classification="BUSINESS_STREET_ADDRESS",
                        contact_name=Name(
                            salutation="MR",
                            first_name="John",
                            middle_name="Lee",
                            last_name="Doe",
                        ),
                        location_name="Baker Plaza",
                    ),
                    chain_level_billing=True,
                    bank_accounts={
                        "key": BankingInfo(
                            account_name="John Doe",
                            bank_name="Wells Fargo",
                            urgent_payment=True,
                            funding_method="NETCREDIT",
                            account_number="20581687",
                            sort_code="121000248",
                            iban="GB48LOYD3037341",
                            swift_code="CPRTGB22",
                            bank_creditor_id="bank_creditor_id_example",
                            bank_direct=True,
                            country="GBR",
                            tape_id="14",
                            true_daily=True,
                            use_chain_account_number=True,
                        ),
                    },
                ),
                distributions={
                    "key": DistributionInfo(
                        method="MAILING",
                        address_type="BUSINESS",
                        email_address="applicant@email.com",
                    ),
                },
                additional_location_info=AdditionalLocationInfo(
                    central_mid="8024999222",
                    central_legal_name="Elavon",
                    central_tax_id="787421357",
                ),
                signed_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                signed_type="WET",
                intermediary_owner_info=IntermediaryOwnerInfo(
                    intermediary_owners=[
                        IntermediaryOwner(
                            ownership_pct="90",
                            business_name="ACME",
                            owner_name=Name(
                                salutation="MR",
                                first_name="John",
                                middle_name="Lee",
                                last_name="Doe",
                            ),
                            phone=PhoneNumber(
                                intl_code="44",
                                area_code="111",
                                number="1231234",
                                extension="2",
                            ),
                            email_address="email_address_example",
                            address=Address(
                                street_name="Baker Street",
                                street_number="221",
                                line_two="Apt B",
                                line_three="48",
                                city="Atlanta",
                                county="Fulton",
                                post_code="30346",
                                country="USA",
                                state="USA_AL",
                                classification="BUSINESS_STREET_ADDRESS",
                                contact_name=Name(
                                    salutation="MR",
                                    first_name="John",
                                    middle_name="Lee",
                                    last_name="Doe",
                                ),
                                location_name="Baker Plaza",
                            ),
                        ),
                    ],
                    additional_intermediate_owners=True,
                ),
                revenue_share_info=RevenueShareInfo(
                    secondary_sales_person="12345",
                    split_percentage="50",
                ),
                elavon_contract="UK",
                internal_use_info=InternalUseInfo(
                    field_auto_info=FieldAutoInfo(
                        requested=True,
                        applied=True,
                        monitored=True,
                        values_modified=True,
                        field_auto_reference_id="field_auto_reference_id_example",
                    ),
                    sales_rep_info=SalesRepInfo(
                        sales_rep_code="12345",
                        name="name_example",
                        email="repname@email.com",
                        submitted=True,
                    ),
                    tin_applied_to_all=True,
                    ip_address="ip_address_example",
                ),
                eframe_info=EframeInfo(
                    scheme_selection="scheme_selection_example",
                    pos_contract=True,
                    is_girocard=True,
                ),
                partner_info=PartnerInfo(
                    partner_name="partner_name_example",
                    associate_id="associate_id_example",
                    book_of_business="book_of_business_example",
                    correlation_id="correlation_id_example",
                    partner_source="partner_source_example",
                    merchant_user_id="merchant_user_id_example",
                    session_id="session_id_example",
                ),
                alternative_payment_methods=[
                    ApmAcquirer(
                        acquirer_code="acquirer_code_example",
                        acquirer_types=[
                            ApmAcquirerType(
                                type_code="type_code_example",
                                per_item_amount="per_item_amount_example",
                                rate_percentage="rate_percentage_example",
                                pricing_tiers=[
                                    ApmPricingTier(
                                        combining_code="combining_code_example",
                                        per_item_amount="per_item_amount_example",
                                        rate_percentage="rate_percentage_example",
                                        description="description_example",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            language="language_example",
            agreement_id="agreement_id_example",
            is_grouped_application=True,
            wet_signed=True,
            card_volume=CardVolume(
                visa_percentage="15.6",
                master_card_percentage="12.3",
                amex_percentage="4.5",
                amex_average_transaction="10.1",
                interac_average_transaction="23.4",
            ),
            vendor_info=ProviderInfo(
                representative_name="Alex Smith",
                representative_email="asmith@email.com",
                representative_sales_code="12345",
                representative_contact_number=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
            ),
            acting_intermediary_info=ActingIntermediaryInfo(
                acting_intermediary_name="acting_intermediary_name_example",
                acting_intermediary_type="QUALIFIED_INTERMEDIARY",
            ),
            bank_account_details_map={
                "key": BankAccountAdditionalInfo(
                    bank_name="bank_name_example",
                    bank_branch="bank_branch_example",
                    direct_debit_authorized=True,
                ),
            },
            is_tax_exempt_equipment=True,
            talech_egift_only=True,
            displayed_currency="displayed_currency_example",
            additional_description_info=AdditionalDescriptionInfo(
                previous_processor_description="Bank of America",
                monetary_pricing_program_description="MIF Unblended",
                referrer_reference_description="referrer_reference_description_example",
                notes="notes_example",
            ),
            additional_value_added_service_info=ValueAddedServices(
                ecs=ElectronicCheckService(
                    reporting_fee=3.14,
                    reporting_num_users="reporting_num_users_example",
                    ach_check_questions=AchCheckQuestions(
                        payment_acceptance_type="payment_acceptance_type_example",
                        prior_acceptance_authorization=True,
                        customer_identification=True,
                        ach_customer_type="EXISTING",
                        maintain_and_disclose_cancel=True,
                        ensure_accurate_transaction_info=True,
                    ),
                ),
                fanfare=Fanfare(
                    setup_fee=1.1,
                    monthly_fee=0.06,
                    annual_fee=1.6,
                    custom_card_upgrade_fee=0.02,
                    included_cards=FanfareCardSplits(
                        promotional="promotional_example",
                        loyalty="loyalty_example",
                        gift="gift_example",
                    ),
                    additional_cards_type="FF_STANDARD",
                    additional_cards=FanfareCardSplits(
                        promotional="promotional_example",
                        loyalty="loyalty_example",
                        gift="gift_example",
                    ),
                    additional_card_price=3.14,
                    program_checkup=3.14,
                    card_style="card_style_example",
                    justification_type="LEFT",
                    card_is_text=True,
                    card_text="card_text_example",
                    text_case_type="TITLE_CASE",
                    text_color="text_color_example",
                    text_font="text_font_example",
                ),
            ),
            additional_business_info=AdditionalBusinessInfo(
                ownership_years_over_range="3",
                is_max_establishment_year=True,
                has_government_incentive=True,
            ),
            funding_type="STANDARD",
            integrator_solution_info=IntegratorSolutionInfo(
                health_care_eligibility_selection_map={
                    "key": HealthCareEligibilityInfo(
                        monthly_fee=0.0,
                        npi_numbers=[
                            "npi_numbers_example",
                        ],
                    ),
                },
                payments=Payments(
                    pms_vendor_pas="pms_vendor_pas_example",
                    number_of_providers="1",
                    sales_rep_phone_number="sales_rep_phone_number_example",
                    integrator_notes="1111111111",
                    has_payment_plans=True,
                ),
                has_ecs_only=True,
                sku="310T3",
            ),
            additional_lease_info=AdditionalLeaseInfo(
                lease_details_map={
                    "key": LeaseDetails(
                        alternate_price=3.14,
                        pricing_plan="pricing_plan_example",
                    ),
                },
            ),
            marketing_data_consent_map={
                "key": True,
            },
            additional_site_survey_info=AdditionalSiteSurveyInfo(
                incomplete_survey_reason_type="NOT_OPEN",
                site_survey_date=DateComponents(
                    year=1970,
                    month="JAN",
                    day=15,
                ),
                site_survey_conducted_by="site_survey_conducted_by_example",
                description_of_no_site_survey="description_of_no_site_survey_example",
            ),
            kyc_quiz_status_map={
                "KYC_RESULT_FAILED_QUIZ": "KYC_RESULT_FAILED_QUIZ",
            },
            var_other_details=VarOtherDetails(
                var_type="VENDOR_DISTRIBUTED",
                vendor="vendor_example",
                product="product_example",
                version="version_example",
            ),
            additional_card_pricing_info=AdditionalCardPricingInfo(
                minimum_card_fee=0.0,
                clear_and_simple_type="clear_and_simple_type_example",
                c4_pricing_type="c4_pricing_type_example",
                high_risk_cost_additional_loading="high_risk_cost_additional_loading_example",
            ),
            sales_office_contact=SalesOfficeContact(
                address=Address(
                    street_name="Baker Street",
                    street_number="221",
                    line_two="Apt B",
                    line_three="48",
                    city="Atlanta",
                    county="Fulton",
                    post_code="30346",
                    country="USA",
                    state="USA_AL",
                    classification="BUSINESS_STREET_ADDRESS",
                    contact_name=Name(
                        salutation="MR",
                        first_name="John",
                        middle_name="Lee",
                        last_name="Doe",
                    ),
                    location_name="Baker Plaza",
                ),
                phone=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
            ),
            sales_person_contact=SalesPersonContact(
                name=Name(
                    salutation="MR",
                    first_name="John",
                    middle_name="Lee",
                    last_name="Doe",
                ),
                phone=PhoneNumber(
                    intl_code="44",
                    area_code="111",
                    number="1231234",
                    extension="2",
                ),
                email_address="email_address_example",
            ),
            additional_auth_pricing_program_info=AdditionalAuthPricingProgramInfo(
                description="description_example",
                fee=5.0,
                auth_amount=10.0,
            ),
            applicant_email="applicant_email_example",
            partner_document_data={
                "key": {
                    "key": "key_example",
                },
            },
            application_id=1,
        ),
    ) # UpdateDocumentPacketDataRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update document packet
        api_response = api_instance.update_document_packet_data(body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->update_document_packet_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateDocumentPacketDataRequest**](UpdateDocumentPacketDataRequest.md)|  |

### Return type

[**UpdateDocumentPacketDataResponse**](UpdateDocumentPacketDataResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Update Document Packet Data Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_document_xsd_schema**
> upload_document_xsd_schema(version_number)

Get Upload Documents Schema

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    version_number = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get Upload Documents Schema
        api_instance.upload_document_xsd_schema(version_number)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->upload_document_xsd_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_number** | **int**|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_documents**
> UploadDocumentResponse upload_documents(version_number, body)

Upload Documents

### Example

* Basic Authentication (basicAuth):

```python
import time
import elavon
from elavon.api import satidapi_api
from elavon.model.upload_documents_request_params import UploadDocumentsRequestParams
from elavon.model.upload_document_response import UploadDocumentResponse
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = elavon.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = elavon.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with elavon.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satidapi_api.SATIDAPIApi(api_client)
    version_number = 1 # int | 
    body = UploadDocumentsRequestParams(
        boarding_id="2101491576",
        client_id="IDNA",
        unique_id="AcmeCorp1572566399123",
        country="country_example",
        sales_rep_number="12345",
        image_document_data=ImageDocumentData(
            doc_reference_number="doc_reference_number_example",
            image_documents=[
                ImageDocument(
                    image_id=1,
                    image_type_code="APPLI",
                    dba_name="Grimm's Bookstore",
                    scan_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    mime_type_code="JPG",
                    image_content=[
                        'YQ==',
                    ],
                    additional_document_fields=[
                        AdditionalDocumentFields(
                            label_code="label_code_example",
                            label_value="label_value_example",
                        ),
                    ],
                    name="name_example",
                    category="AML_OTHER",
                ),
            ],
        ),
    ) # UploadDocumentsRequestParams | 

    # example passing only required values which don't have defaults set
    try:
        # Upload Documents
        api_response = api_instance.upload_documents(version_number, body)
        pprint(api_response)
    except elavon.ApiException as e:
        print("Exception when calling SATIDAPIApi->upload_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_number** | **int**|  |
 **body** | [**UploadDocumentsRequestParams**](UploadDocumentsRequestParams.md)|  |

### Return type

[**UploadDocumentResponse**](UploadDocumentResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Standard Upload Document Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

