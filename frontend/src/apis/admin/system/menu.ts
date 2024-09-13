import request from "@/utils/request";

export const getAllMenuList = async () => {
  try {
    const res = await request.get("/api/admin/system/menu");
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getAllMenuTree = async () => {
  try {
    const res = await request.get("/api/admin/system/menu/tree");
    return res;
  } catch (error) {
    console.error(error);
  }
};
