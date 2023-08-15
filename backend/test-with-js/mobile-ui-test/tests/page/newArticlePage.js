let NewArticlePage = {
    titleInput: $('input[ng-model="$ctrl.article.title"]'),
    descriptionInput: $('input[ng-model="$ctrl.article.description"]'),
    bodyInput: $('textarea[ng-model="$ctrl.article.body"]'),
    publishButton: $('button[type="submit"]'),

    async goToNewArticle() {
        await browser.url('https://angular.realworld.io/editor');
    },

    async publishArticle(title, description, body) {
        await this.titleInput.setValue(title);
        await this.descriptionInput.setValue(description);
        await this.bodyInput.setValue(body);
        await this.publishButton.click();
    }
}

module.exports = NewArticlePage;
