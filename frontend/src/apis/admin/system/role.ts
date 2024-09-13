import request from "@/utils/request";

export const getAllRoles = async () => {
  try {
    const res = await request.get("/api/admin/system/role");
    return res;
  } catch (error) {
    console.error(error);
  }
};
