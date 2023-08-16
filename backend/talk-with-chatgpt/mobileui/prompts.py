from langchain import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

WRITE_MOBILE_LOCATOR = """
Write mobile ui auto test with {client_tool}  for {platform} base on mobile screen layout and given selectors,write all locator together, do not write explanatory information.

===SELECTOES===
ACCESSIBILITY ID SELECTOR
example is: const elem = await $('~my_accessibility_identifier')
For ios it is accessibilityIdentifier
For android it is android:contentDescription="@string/inspect"

ANDROID UIAUTOMATOR SELECTOR
it is only for Android, the selector example is: 
const element = await $(`android=$new UiSelector().text("Cancel").className("android.widget.Button")`)
const element = await $('android=new UiSelector().resourceId("your_resource_id")')

IOS UIAUTOMATION LOCATOR SELECTOR
it is only for iOS, the selector example is:
const element = await $(`ios=UIATarget.localTarget().frontMostApp().mainWindow().buttons()[0]`)

IOS XCUITEST PREDICATE STRINGS AND CLASS CHAINS SELECTOR
It is only for iOS, the selector example is:
const element = await $(`-ios predicate string:type == 'XCUIElementTypeSwitch' && name CONTAINS 'Allow'`)
const element = await $(`-ios class chain:**/XCUIElementTypeCell[`name BEGINSWITH "D"`]/**/XCUIElementTypeButton`)

CLASS NAME SELECTOR
For iOS it is the full name of a UIAutomation class, and will begin with UIA-, such as UIATextField for a text field, such as as $('UIATextField').click()
For Android it is the fully qualified name of a UI Automator class, such android.widget.EditText for a text field, such as await $('android.widget.DatePicker').click()

CLASS CHAIN SELECTOR
For iOS, the example is : 
const element = await $(`-ios class chain:**/XCUIElementTypeTextField[`name="username"`]`)
For Android, the example is: 
const element = await $('~parentClassName parentIndex=0 ~childClassName childIndex=1')

XPATH SELECTOR
For iOS, the example is: 
const element = await $('//XCUIElementTypeTextView[@name="textContent"]')
For Android,the example is:
const element = await $('//android.widget.TextView[@text="textContent"]')
===END OF SELECTORS===

===MOBILE SCREEN LAYOUT===
{layout}
===END OF MOBILE SCREEN LAYOUT===

Write reasonable mobile app ui locator with following guideline:
1.The mobile app is {platform},  Review the provided selectors and choose the most suitable selector to locate each element. Note that certain selectors are intended for iOS only, some for Android only, and others for both iOS and Android platforms.
2.Analyze the layout of the mobile screen, and consider which selector would be the most appropriate to uniquely identify each element.

Task: Generate locators for all elements based on the provided mobile screen layout. Ensure that a locator is provided for each element on the mobile screen layout.
"""

template = "You are an mobile ui auto test expert,write reasonable locator base on mobile screen layout and given selector."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = WRITE_MOBILE_LOCATOR
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
mobileui_locator_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])

WRITE_MOBILE_STEP_FUNCTION = """
Write test case with {client_tool} base on test step description, use provide page locators,do not generate page locator by yourself.
===PAGE LOCATOR
{locators}
===END OF PAGE LOCATOR

===TEST STEP DESCRIPTION
{test_step_description}
===END OF TEST STEP DESCRIPTION
"""
template = "You are an mobile ui auto test expert,write test case with {client_tool} base on page locators and test step description."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = WRITE_MOBILE_STEP_FUNCTION
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
mobileui_step_function_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])
