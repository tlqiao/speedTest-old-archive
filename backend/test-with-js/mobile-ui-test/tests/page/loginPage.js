let LoginPage = {
    emailInput: $('input[formcontrolname="email"]'),
    passwordInput: $('input[formcontrolname="password"]'),
    signInButton: $('button[type="submit"]'),

    async goToSignIn() {
        await browser.url('https://angular.realworld.io/');
        await $('a[href="#login"]').click();
    },

    async signIn() {
        let user = require('./user.json');
        await this.emailInput.setValue(user.username);
        await this.passwordInput.setValue(user.password);
        await this.signInButton.click();
    }
}

module.exports = LoginPage;
