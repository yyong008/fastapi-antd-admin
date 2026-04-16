import request from "@/utils/request";

type LoginData = {
  username: string;
  password: string;
};

type RegisterData = {
  username: string;
  password: string;
  email?: string;
};

export const login = async (data: LoginData) => {
  try {
    const res = await request.post("/api/auth/login", data, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const register = async (data: RegisterData) => {
  try {
    const res = await request.post("/api/auth/register", data);
    return res;
  } catch (error) {
    console.error(error);
  }
};
