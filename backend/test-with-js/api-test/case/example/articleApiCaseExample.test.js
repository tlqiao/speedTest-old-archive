import {getArticle,addArticle} from "../../api/example/articleApiCallExample.js";

describe('article test',() => {
    it('it should get articles successfully',async() => {
        const response = await getArticle();
        expect(response.statusCode).toBe(200)
    })
    it('it should create article successfully', async() => {
        const title = 'title' + Math.floor(Math.random());
        const response = await addArticle(title)
        expect(response.statusCode).toBe(200)
    })
})
