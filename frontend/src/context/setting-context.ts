import { createContext } from "react";

const SettingContext = createContext({
  theme: {
    colorPrimary: "",
    // layout: "mix"
  },
  setTheme: () => {},
});

export default SettingContext;
