import request from "@/utils/request";

export const createSignInLog = async () => {
  try {
    const res = await request.post("/api/admin/signin_log/");
    return res;
  } catch (error) {
    console.error(error);
  }
};
