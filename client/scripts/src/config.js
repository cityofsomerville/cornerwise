/**
 * config.js
 *
 * Application configuration options
 */

define(["optional!localConfig", "underscore", "messages"], function(localConfig, _, messages) {
    var config = {
        // String template or function used by Leaflet to generate the
        // image URLs for map files.
        tilesURL: "https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}@2x.png",
        tilesCredit: "Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL",

        backendURL: "",

        // Lat/long for the southwest and northeasth corners of the
        // map's initial viewing area.
        bounds:  [[42.37236882604975, -71.14565849304199],
                  [42.41680352972898, -71.04806900024413]],

        regionBounds: null,

        // Default reference location:
        refPointDefault: {lat: 42.387545768736246,
                          lng: -71.09950304031372},
        refPointName: "City Hall",

        // Configuration for subscriptions:
        // See: http://leafletjs.com/reference-1.3.0.html#circle-option
        subscribeCircleStyle: {
            stroke: true,
            weight: 2,
            color: "green",
            fillColor: "gray",
            dashArray: "5, 5"
        },

        // Default values for application state
        stateDefaults: null,

        filters: [
            {
                "name": "Application Status",
                "key": "status",
                "type": "select",
                "options": [
                    {"value": "active", "name": "Pending"},
                    {"value": "closed", "name": "Complete"},
                    {"value": "all", "name": "All"},
                ]
            }
        ],

        proposalAttributes: [
            "applicant",
            "owner",
            "recommendation",
            "decision"
        ],

        proposalDocumentGroups: null,
        // Example:
        // proposalDocumentGroups: [
        //     {name: "Staff Documents", tags: ["reports", "decisions"]},
        //     {name: "Application Documents", tags: ["other"]}
        // ],

        showProposalImages: true,

        // The style that will be applied to the rectangle representing the
        // bounds of the current area filter:
        filterBoundsStyle: {
            weight: 2,
            color: "red",
            fillColor: "red",
            fillOpacity: "0"
        },

        defaultProposalThumb: "/static/images/marker-normal@2x.png",

        regions: [
            {
                id: "somerville",
                name: "Somerville, MA",
                source: "/static/layerdata/somerville.geojson",
                city: "Somerville",
                state: "MA"
            },
            {
                id: "cambridge",
                name: "Cambridge, MA",
                source: "/static/layerdata/cambridge.geojson",
                city: "Cambridge",
                state: "MA"
            }
        ],

        // Specify the ids of regions to include
        includeRegions: null,
        // For geocoding:


        regionStyle: {
            weight: 3,
            color: "#4fb8f7",
            fillColor: "#4fb8f7",
            fillOpacity: 0.15
        },

        contacts: [],
        codeReference: {
            "Somerville, MA": {
                url: "https://xref.cornerwise.org/somervillema?ordinance_section={section}",
                pattern: "§(\\d+(?:\\.\\d+)+)"
            },
            "Cambridge, MA": null
        },

        caseLink: {
            "Somerville, MA": {
                pattern: "((?:ZBA|PB)\\s?(?:(?:[\\dA-Z]+-)+(?:[\\dA-Z]+)))"
            }
        },

        messages: messages,

        layers: [
            {
                source: "/static/scripts/src/layerdata/glx.geojson",
                id: "glx",
                icon: "glx",
                iconCredit: "Scott de Jonge",
                title: "Train - Green Line Extension",
                short: "Train",
                info: "The Green Line Extension plans to bring light rail services to areas of Somerville and Medford currently underserved by the MBTA.",
                template:
                ('<strong><%= title %></strong>' +
                 '<br>Scheduled Opening: ' +
                 '<%= monthEstimate + "/" + yearEstimate %>' +
                 '<br><a href="<%= factSheet %>" target="_blank">Fact Sheet</a>'),
                color: "green",
                shown: false,
                marker: {
                    type: "circle",
                    color: "green",
                    fillColor: "white",
                    radius: 5,
                    fillOpacity: 1
                },
                features: null
            },
            // {
            //     source: "/static/scripts/src/layerdata/community_path.geojson",
            //     id: "cp",
            //     info: "The Somerville Community Path is a paved bike and walking path. It begins at Davis Square, where it connects to the Cambridge Linear Path, and ends at Lowell Street. Once extended, it will end at NorthPoint, Cambridge.",
            //     title: "Community Path Extension",
            //     color: "orange",
            //     shown: false,
            //     features: null
            // },
            {
                source: "https://raw.githubusercontent.com/cityofsomerville/geodata/master/neighborhoods.geojson",
                id: "neighborhoods",
                icon: "home",
                info: "Approximate and unofficial neighborhood boundaries",
                iconCredit: "Freepik",
                title: "Neighborhood Boundaries",
                short: "Neighborhoods",
                color: "blue",
                shown: false,
                features: null,
                template: "<%= title %>"
            },
            {
                source: "https://raw.githubusercontent.com/cityofsomerville/geodata/master/wards.geojson",
                id: "District",
                icon: "District",
                iconCredit: "Scott de Jonge",
                info: "Somerville is divided into seven District, each represented by an alderman.",
                title: "District",
                short: "District",
                color: "pink",
                shown: false,
                features: null,
                template: "<%= title %>"
            }
        ],

        // TODO: Respect this value
        showParcelsAboveZoomLevel: 15,

        parcelStyle: {
            stroke: 0.5,
            color: "orange"
        },

        // Esri:
        clientId: "jYLY7AeA1U9xDiWu",
        clientSecret: "64a66909ff724a0a9928838ef4462909",

        // Error messages:
        errors: {
            geolocation: {
                unavailable: "Geolocation unavailable in your browser.",
                denied: "Could not set location without your permission.",
                unavailable: "Could not determine your position",
                timeout: "Geolocation took too long."
            }
        },

        // Map of handles to names
        attributeNames: {

        }
    };

    if (localConfig) {
        _.extend(config, localConfig);
    }


    if (window["SITE_CONFIG"]) {
        Array.prototype.push.apply(config.filters, SITE_CONFIG.extra_filters);
        delete SITE_CONFIG["extra_filters"];
        _.extend(config.messages, SITE_CONFIG.messages);
        delete SITE_CONFIG["messages"];
        _.extend(config, window["SITE_CONFIG"]);
    }

    return config;
});
