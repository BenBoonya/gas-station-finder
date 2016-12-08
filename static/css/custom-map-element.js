import React, {StyleSheet, Dimensions, PixelRatio} from "react-native";
const {width, height, scale} = Dimensions.get("window"),
    vw = width / 100,
    vh = height / 100,
    vmin = Math.min(vw, vh),
    vmax = Math.max(vw, vh);

export default StyleSheet.create({
    "gas-station-layout": {
        "backgroundColor": "white",
        "width": 300,
        "textAlign": "left",
        "position": "absolute",
        "left": 60,
        "top": 20,
        "border": "1px solid #dddddd",
        "borderRadius": 5,
        "boxSizing": "border-box",
        "paddingTop": 10,
        "paddingRight": 10,
        "paddingBottom": 10,
        "paddingLeft": 10
    },
    "near-by-station": {
        "paddingTop": 10,
        "paddingRight": 10,
        "paddingBottom": 10,
        "paddingLeft": 10
    },
    "locationButton": {
        "backgroundColor": "white",
        "border": 1,
        "borderColor": "grey",
        "color": "grey",
        "textAlign": "center",
        "textDecoration": "none",
        "display": "block",
        "fontSize": 16,
        "marginTop": 4,
        "marginRight": 2,
        "marginBottom": 4,
        "marginLeft": 2,
        "cursor": "pointer"
    }
});