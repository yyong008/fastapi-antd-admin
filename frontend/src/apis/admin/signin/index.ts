import request from "@/utils/request";

export const signin = async (data: any) => {
  try {
    const res = await request.post("/auth/signin/", data);
    return res;
  } catch (error) {
    console.error(error);
  }
};
