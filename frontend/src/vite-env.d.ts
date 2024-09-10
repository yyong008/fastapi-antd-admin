/// <reference types="vite/client" />
import type packageJSON from '../package.json';

declare global {
  const __APP_INFO__: {
    pkg: typeof packageJSON;
    lastBuildTime: string;
  };
}

