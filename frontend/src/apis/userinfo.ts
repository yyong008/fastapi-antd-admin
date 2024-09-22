import request from "@/utils/request";

export const getUserInfo = async () => {
  try {
    const res = await request.get("/api/admin/userinfo");
    return res;
  } catch (error) {
    console.error(error);
  }
};
