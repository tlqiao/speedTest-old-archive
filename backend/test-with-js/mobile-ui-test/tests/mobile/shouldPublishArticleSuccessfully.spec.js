const LoginPage = require('../page/loginPage');
const NewArticlePage = require('../page/newArticlePage');
const SettingPage = require('../page/settingPage');

describe('Publishing Article Test', function() {
    it('should publish article successfully', async function() {
        await LoginPage.goToSignIn();
        await LoginPage.signIn();
        await NewArticlePage.goToNewArticle();
        await NewArticlePage.publishArticle('Title', 'Description', 'Body');
        await SettingPage.goToSettings();
        await SettingPage.logout();
    });
});
