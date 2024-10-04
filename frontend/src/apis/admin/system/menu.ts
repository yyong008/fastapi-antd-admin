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

export const getAllMenuTreeNoPermission = async () => {
  try {
    const res = await request.get("/api/admin/system/menu/tree/no-permission");
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getMenuById = async (id: number) => {
  try {
    const res = await request.get(`/api/admin/system/menu/${id}`);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const createMenu = async (data: any) => {
  try {
    const res = await request.post("/api/admin/system/menu", data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const updateMenu = async (id: number, data: any) => {
  try {
    const res = await request.put("/api/admin/system/menu/" + id, data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const deleteMenuByIds = async (ids: number[]) => {
  try {
    const res = await request.delete(`/api/admin/system/menu/`, {
      data: {
        ids
      }
    });
    return res;
  } catch (error) {
    console.error(error);
  }
}
