import request from "@/utils/request";

export const getUsers = async (searchParams) => {
  try {
    const res = await request.get("/api/admin/system/user", {
      params: { page: searchParams.page, pageSize: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getUserById = async (id) => {
  try {
    const res = await request.get(`/api/admin/system/user/${id}`);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const createUser = async (data) => {
  try {
    const res = await request.post("/api/admin/system/user", data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const updateUser = async (id, data) => {
  try {
    const res = await request.put(`/api/admin/system/user/${id}`, data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const deleteUser = async (id) => {
  try {
    const res = await request.delete(`/api/admin/system/user/${id}`);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const deleteUserByIds = async (ids) => {
  try {
    const res = await request.delete(`/api/admin/system/user/`, {
      data: { ids }
    });
    return res;
  } catch (error) {
    console.error(error);
  }
}
