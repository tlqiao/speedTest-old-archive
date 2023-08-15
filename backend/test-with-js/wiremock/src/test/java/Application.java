import com.github.tomakehurst.wiremock.WireMockServer;
import com.github.tomakehurst.wiremock.core.WireMockConfiguration;

import static com.github.tomakehurst.wiremock.client.WireMock.*;

public class Application {
    private static final int MOCK_SERVER_PORT = 8080;

    public static void main(String[] args) {
        WireMockServer wireMockServer = new WireMockServer
                (WireMockConfiguration.options()
                        .port(MOCK_SERVER_PORT)
                        .usingFilesUnderClasspath("mock"));
        wireMockServer.start();
        System.out.println("WireMock server started on port " + MOCK_SERVER_PORT);
        configureMockMappings(wireMockServer);
    }
    private static void configureMockMappings(WireMockServer wireMockServer) {
        wireMockServer.stubFor(get(urlEqualTo("/api/sample"))
                .willReturn(aResponse()
                        .withStatus(200)
                        .withBody("Mocked response from WireMock")));
        wireMockServer.stubFor(get(urlPathEqualTo("/search"))
                .withQueryParam("name", equalTo("li"))
                .willReturn(aResponse()
                        .withStatus(200)
                        .withBody("search response fromWireMock")));
//mock multiple server api by proxy
//use real server api by proxy
        wireMockServer.stubFor(get(urlMatching("/api/other/.*"))
                .willReturn(aResponse().proxiedFrom("http://localhost:9091")));
        //proxy to another server base on api path
        String[] apiPaths = {
                "/api/another/one",
                "/api/another/two",
                "/api/another/three"
        };
        // Create stubs for each API URL path in the array
        for (String path : apiPaths) {
            wireMockServer.stubFor(get(urlMatching(path))
                    .willReturn(aResponse().proxiedFrom("http://localhost:9090")));
        }
    }
}
