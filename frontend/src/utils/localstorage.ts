const TOKEN = "token"
const REFRESH_TOKEN = "refresh_token"

export const setLocalStorageToken = (token: string) =>
  localStorage.setItem(TOKEN, token);
export const getLocalStorageToken = () => localStorage.getItem(TOKEN);
export const removeLocalStorageToken = () => localStorage.removeItem(TOKEN);

export const setLocalStorageRefreshToken = (refresh_token: string) =>
  localStorage.setItem(REFRESH_TOKEN, refresh_token);
export const getLocalStorageRefreshToken = () =>
  localStorage.getItem(REFRESH_TOKEN);
export const removeLocalStorageRefreshToken = () =>
  localStorage.removeItem(REFRESH_TOKEN);
