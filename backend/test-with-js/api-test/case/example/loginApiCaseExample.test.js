import {login} from '../../api/example/loginApiCallExample.js'

describe('test login', () => {
    it.each([{email: 'demotest@163.com', password: '123456', status: 200},
        {email: 'demotest@163.com', password: 'wrong', status: 403}
    ])('should login correctly', async ({email, password, status}) => {
        const response = await login(email, password)
        expect(response.statusCode).toBe(status)
    })
})
