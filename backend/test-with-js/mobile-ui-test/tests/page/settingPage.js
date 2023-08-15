let SettingPage = {
    logoutButton: $('a[href="#/logout"]'),

    async goToSettings() {
        await $('a[href="#settings"]').click();
    },

    async logout() {
        await this.logoutButton.click();
    }
}

module.exports = SettingPage;
