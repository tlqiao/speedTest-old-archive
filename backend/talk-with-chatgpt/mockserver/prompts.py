from langchain import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

WRITE_MAPPING_FILE = """
Write wiremock mapping file base on  API Details.

===API DETAILS===
API_URL: {api_url}
API_METHOD: {api_method}
API_REQUEST_BODY: {api_request}
API RESPONSE:{api_response}
IS_MATCH_COOKIE: {is_map_cookie}
IS_MATCH_HEADER: {is_map_header}
===END OF API DETAILS===
Write reasonable wiremock mapping file with following format:

1: Analysis API Details's API_URL, if find queryParameters, use matches,doesNotMatch rules to match api query parameters  when generating the wiremock mapping files, if there is no queryparameter, mappingfile can not include query parameters match.
2: Analysis API Details's API_REQUEST_BODY, if it is not null, use equalToJson rule to match api request body when generating the wiremock mapping files.
3: Analysis API Details's IS_MATCH_COOKIE, if  IS_MATCH_COOKIE is true, use cookies contains xxxx rules to match cookie when generating the wiremock mapping files, if IS_MATCH_COOKIE is false, mappingfile can not include cookie match.
4: Analysis API Details's IS_MATCH_HEADER, if IS_MATCH_HEADER is true, use Content-Type  equalTo, caseInsensitive: true/false to match api header when generating the wiremock mapping files, if IS_MATCH_HEADER is false, mapping file can not include header match.

Tasks: Write wire mock mapping file base on above thought.
"""


WRITE_MAPPING_FILE_WITH_REGEX = """
Write wiremock mapping file base on wiremock mapping rules with regex and API Details.

===API DETAILS===
API_URL: {api_url}
API_METHOD: {api_method}
API_REQUEST_BODY: {api_request}
API RESPONSE:{api_response}
IS_MATCH_COOKIE: {is_map_cookie}
IS_MATCH_HEADER: {is_map_header}
===END OF API DETAILS===
Write reasonable wiremock mapping file with following format:

1: Analysis API Details's API_URL, if find queryParameters, use matches,doesNotMatch rules to match api query parameters  when generating the wiremock mapping files, if there is no queryparameter, mappingfile can not include query parameters match.
2: Analysis API Details's API_REQUEST_BODY, if it is not null, use matchesJsonPath rule to match api request body when generating the wiremock mapping files.
3: Analysis API Details's IS_MATCH_COOKIE, if  IS_MATCH_COOKIE is true, use cookies contains xxxx rules to match cookie when generating the wiremock mapping files, if IS_MATCH_COOKIE is false, mappingfile can not include cookie match.
4: Analysis API Details's IS_MATCH_HEADER, if IS_MATCH_HEADER is true, use Content-Type  equalTo, caseInsensitive: true/false to match api header when generating the wiremock mapping files, if IS_MATCH_HEADER is false, mapping file can not include header match.

Tasks: Write wire mock mapping file base on above thought.
"""
template = "You are an wiremock expert,wite wiremock mapping file, return it with json format"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = WRITE_MAPPING_FILE
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
generate_mapping_file_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])

human_template = WRITE_MAPPING_FILE_WITH_REGEX
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
generate_mapping_file_with_regex_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])
