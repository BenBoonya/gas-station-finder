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
        "right": 10,
        "bottom": 30,
        "border": "1px solid #dddddd",
        "borderRadius": 5,
        "boxSizing": "border-box"
    },
    "title": {
        "position": "absolute",
        "left": 3
    }
});