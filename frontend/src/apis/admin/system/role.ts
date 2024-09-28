import request from "@/utils/request";

export const getAllRoles = async () => {
  try {
    const res = await request.get("/api/admin/system/role");
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getRoleById = async (id: number) => {
  try {
    const res = await request.get(`/api/admin/system/role/${id}`);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const createRole = async (data: any) => {
  try {
    const res = await request.post("/api/admin/system/role", data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const updateRole = async (id: number, data: any) => {
  try {
    const res = await request.put(`/api/admin/system/role/${id}`, data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const deleteRoleByIds = async (ids: number[]) => {
  try {
    const res = await request.delete(`/api/admin/system/role/`, {
      data: {
        ids
      }
    });
    return res;
  } catch (error) {
    console.error(error);
  }
}
