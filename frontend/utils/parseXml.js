export function parseXmlToString(xmlContent) {
    const trimmedLines = xmlContent.split('\n').map(line => line.trim());
    const convertedString = trimmedLines.join('\n').replace(/"/g, "'");
    console.log(convertedString);
}

const xmlContent="<body>\n" +
    "    <app-root ng-version=\"7.2.4\">\n" +
    "        <app-editor-page>\n" +
    "            <div class=\"editor-page\">\n" +
    "                <div class=\"container page\">\n" +
    "                    <div class=\"row\">\n" +
    "                        <div class=\"col-md-10 offset-md-1 col-xs-12\">\n" +
    "                            <app-list-errors><!---->\n" +
    "                                <ul class=\"error-messages\"><!----></ul>\n" +
    "                            </app-list-errors>\n" +
    "                            <form novalidate=\"\" class=\"ng-untouched ng-pristine ng-valid\">\n" +
    "                                <fieldset>\n" +
    "                                    <fieldset class=\"form-group\">\n" +
    "                                        <input class=\"form-control form-control-lg ng-untouched ng-pristine ng-valid\"\n" +
    "                                               formcontrolname=\"title\" placeholder=\"Article Title\" type=\"text\">\n" +
    "                                    </fieldset>\n" +
    "                                    <fieldset class=\"form-group\">\n" +
    "                                        <input class=\"form-control ng-untouched ng-pristine ng-valid\"\n" +
    "                                               formcontrolname=\"description\" placeholder=\"What's this article about?\"\n" +
    "                                               type=\"text\">\n" +
    "                                    </fieldset>\n" +
    "                                    <fieldset class=\"form-group\">\n" +
    "                                        <textarea class=\"form-control ng-untouched ng-pristine ng-valid\"\n" +
    "                                                  formcontrolname=\"body\" placeholder=\"Write your article (in markdown)\"\n" +
    "                                                  rows=\"8\"></textarea>\n" +
    "                                    </fieldset>\n" +
    "                                    <fieldset class=\"form-group\">\n" +
    "                                        <input class=\"form-control ng-untouched ng-pristine ng-valid\"\n" +
    "                                               placeholder=\"Enter tags\" type=\"text\">\n" +
    "                                        <div class=\"tag-list\"><!----></div>\n" +
    "                                    </fieldset>\n" +
    "                                    <button class=\"btn btn-lg pull-xs-right btn-primary\" type=\"button\">Publish Article\n" +
    "                                    </button>\n" +
    "                                </fieldset>\n" +
    "                            </form>\n" +
    "                        </div>\n" +
    "                    </div>\n" +
    "                </div>\n" +
    "            </div>\n" +
    "        </app-editor-page>\n" +
    "</body>"

parseXmlToString(xmlContent)
