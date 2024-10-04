import request from "@/utils/request";

type TDepts = {
  page: number;
  pageSize: number;
};

export const getDepts = async (searchParams: TDepts) => {
  try {
    const res = await request.get("/api/admin/system/dept", {
      params: { page: searchParams.page, pageSize: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getDeptById = async (id: number) => {
  try {
    const res = await request.get(`/api/admin/system/dept/${id}`);
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const createDept = async (data: any) => {
  try {
    const res = await request.post("/api/admin/system/dept", data);
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const updateDept = async (id: number, data: any) => {
  try {
    const res = await request.put(`/api/admin/system/dept/${id}`, data);
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const deleteDeptByIds = async (ids: number[]) => {
  try {
    const res = await request.delete(`/api/admin/system/dept/`, {
      data: { ids },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};
