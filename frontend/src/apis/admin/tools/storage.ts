import request from "@/utils/request";

type TDepts = {
  page: number;
  pageSize: number;
};

export const getToolsStorage = async (searchParams: TDepts) => {
  try {
    const res = await request.get("/api/admin/tools/storage/", {
      params: { page: searchParams.page, pageSize: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};


export const getToolsStorageById = async (id: number) => {
  try {
    const res = await request.get(`/api/admin/tools/storage/${id}`);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const createToolsStorage = async (data: any) => {
  try {
    const res = await request.post("/api/admin/tools/storage/", data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const updateToolsStorageByIds = async (id: number, data: any) => {
  try {
    const res = await request.put(`/api/admin/tools/storage/${id}`, data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const deleteToolsStorageByIds = async (ids: number[]) => {
  try {
    const res = await request.delete(`/api/admin/tools/storage/`, {
      data: { ids },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
}
