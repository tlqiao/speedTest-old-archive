from flask import Flask, jsonify, request
from cases.chains import write_test_case
from mobileui.chains import write_locator_for_mobile_ui, write_step_function_for_mobile_ui
from webui.chains import write_locators_for_web_ui, write_step_function_for_web_ui
from mockserver.chains import write_mapping_file
from contract.chains import write_contract_test
from unit.chains import write_unit_test

app = Flask(__name__)


@app.route('/chatWithGPT/writeCase', methods=['POST'])
def write_test_case_by_chatGPT():
    requirements = request.get_json().get('requirements')
    language = request.get_json().get('language')
    data = write_test_case(language, requirements)
    response_data = {
        "cases": data
    }
    return jsonify(response_data)


@app.route('/chatWithGPT/writeMobileLocator', methods=['POST'])
def write_mobile_locator_by_chatGPT():
    client_tool = request.get_json().get('clientTool')
    platform = request.get_json().get('platform')
    layout = request.get_json().get('layout')
    data = write_locator_for_mobile_ui(
        client_tool=client_tool, platform=platform, layout=layout)
    response_data = {
        "mobileLocators": data
    }
    return jsonify(response_data)


@app.route('/chatWithGPT/writeWebLocator', methods=['POST'])
def write_web_locator_by_chatGPT():
    test_tool = request.get_json().get('testTool')
    page = request.get_json().get('page')
    data = write_locators_for_web_ui(test_tool, page)
    response_data = {
        "webLocators": data
    }
    return jsonify(response_data)


@app.route('/chatWithGPT/writeWebStepFunction', methods=['POST'])
def write_web_step_function_by_chatGPT():
    test_tool = request.get_json().get('testTool')
    locators = request.get_json().get('locators')
    step_description = request.get_json().get("stepDesc")
    data = write_step_function_for_web_ui(
        test_tool, locators, step_description)
    response_data = {
        "stepFunction": data
    }
    return jsonify(response_data)


@app.route('/chatWithGPT/writeMobileStepFunction', methods=['POST'])
def write_mobile_step_function_by_chatGPT():
    client_tool = request.get_json().get('clientTool')
    locators = request.get_json().get('locators')
    step_description = request.get_json().get("stepDesc")
    data = write_step_function_for_web_ui(
        client_tool, locators, step_description)
    response_data = {
        "stepFunction": data
    }
    return jsonify(response_data)


@app.route('/chatWithGPT/writeMappingFile', methods=['POST'])
def write_mapping_file_by_chatGPT():
    is_map_header = request.get_json().get('isMapHeader')
    is_map_cookie = request.get_json().get('isMapCookie')
    is_use_regex = request.get_json().get("isUseRegex")
    api_details = request.get_json().get("apiDetails")

    data = write_mapping_file(
        is_use_regex, is_map_header, is_map_cookie, api_details)
    return jsonify(data)


@app.route('/chatWithGPT/writeContractTest', methods=['POST'])
def write_contract_test_by_chatGPT():
    test_tool = request.get_json().get('testTool')
    api_details = request.get_json().get("apiDetails")
    result = write_contract_test(
        test_tool, api_details)
    response_data = {
        "data": result
    }
    return jsonify(response_data)


@app.route('/chatWithGPT/writeUnitTest', methods=['POST'])
def write_unit_test_by_chatGPT():
    test_tool = request.get_json().get('testTool')
    language = request.get_json().get("language")
    test_type = request.get_json().get("testType")
    mock_tool = request.get_json().get("mockTool")
    assert_tool = request.get_json().get("assertTool")
    source_code = request.get_json().get("sourceCode")
    result = write_unit_test(
        test_tool, language, mock_tool, test_type, assert_tool, source_code)
    response_data = {
        "unitTest": result
    }
    return jsonify(response_data)

@app.route('/health-check', methods=['GET'])
def hello():
    return "This is talk-with-chatWithGPT server"

# Run the application
if __name__ == '__main__':
    app.run(port=8090)
