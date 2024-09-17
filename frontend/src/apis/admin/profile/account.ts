import request from "@/utils/request";

export const getProfileAccount = async () => {
  try {
    const res = await request.get("/api/admin/profile/account/");
    return res;
  } catch (error) {
    console.error(error);
  }
};
