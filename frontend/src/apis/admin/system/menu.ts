import request from "@/utils/request";

export const getAllMenuList = async () => {
  try {
    const res = await request.get("/api/admin/system/menu");
    return res;
  } catch (error) {
    console.error(error);
  }
};
