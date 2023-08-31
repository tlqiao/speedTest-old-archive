export async function generateCaseCode(apiName, parameterizeFields) {
    let defaultParameters= JSON.stringify(await generateDefaultValue(parameterizeFields))
    console.log(defaultParameters)
    let generateContent = ` import {${apiName}Call} from "./api-test/api/${apiName}Call.js";
describe('test ${apiName}', () => {
    it.each([${defaultParameters}
    ])('should createProfile correctly', async (${parameterizeFields}) => {
        const response = await ${apiName}Call(${parameterizeFields})
        expect(response.statusCode).toBe(200)
    })
}) `
    return generateContent
}
async function generateDefaultValue(parameterizeFields) {
    let defaultValue = "default"
    const result = parameterizeFields.reduce((obj, key) => {
        obj[key] = defaultValue;
        return obj;
    }, {});
    return result
}
