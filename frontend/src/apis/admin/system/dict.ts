import request from "@/utils/request";

type TDict = {
  page: number;
  pageSize: number;
};

export const getDict = async (searchParams: TDict) => {
  try {
    const res = await request.get("/api/admin/system/dict", {
      params: {
        page: searchParams.page,
        pageSize: searchParams.pageSize,
      },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getDictById = async (id: number) => {
  try {
    const res = await request.get(`/api/admin/system/dict/${id}`);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const createDict = async (data: any) => {
  try {
    const res = await request.post("/api/admin/system/dict", data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const updateDict = async (id: number, data: any) => {
  try {
    const res = await request.put(`/api/admin/system/dict/${id}`, data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const deleteDictByIds = async (ids: number[]) => {
  try {
    const res = await request.delete(`/api/admin/system/dict/`, {
      data: {
        ids,
      }
    });
    return res;
  } catch (error) {
    console.error(error);
  }
}
