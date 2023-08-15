import {createProfileCall} from "../api/createProfileCall.js";
describe('test createProfile', () => {
    it.each([{ fullName: 'defaultValue' }
    ])('should createProfile correctly', async ({fullName}) => {
        const response = await createProfileCall(fullName)
        expect(response.statusCode).toBe(200)
    })
})
