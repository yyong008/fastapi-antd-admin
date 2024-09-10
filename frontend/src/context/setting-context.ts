import { createContext } from "react";

const SettingContext = createContext({
  theme: {
    colorPrimary: "",
    // layout: "mix"
  },
  setTheme: (theme: any) => {},
});

export default SettingContext;
