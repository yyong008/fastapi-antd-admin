import request from "@/utils/request";

export const getProfileAccount = async () => {
  try {
    const res = await request.get("/api/admin/profile/account/");
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const updateProfileAccount = async (data: any) => {
  try {
    const res = await request.put("/api/admin/profile/account/", data);
    return res;
  } catch (error) {
    console.error(error);
  }
}
