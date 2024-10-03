import request from "@/utils/request";

type TDict = {
  page: number;
  pageSize: number;
};

export const getDictItem = async (id: number, searchParams: TDict) => {
  try {
    const res = await request.get("/api/admin/system/dict-item/", {
      params: {
        dictId: id,
        page: searchParams.page,
        pageSize: searchParams.pageSize,
      },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getDictItemById = async (id: number) => {
  try {
    const res = await request.get("/api/admin/system/dict-item/" + id);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const createDictItem = async (data: any) => {
  try {
    const res = await request.post("/api/admin/system/dict-item", data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const updateDictItem = async (id: number, data: any) => {
  try {
    const res = await request.put("/api/admin/system/dict-item/" + id, data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const deleteDictItemByIds = async (ids: number[]) => {
  try {
    const res = await request.delete("/api/admin/system/dict-item/", {
      data: {
        ids,
      }
    });
    return res;
  } catch (error) {
    console.error(error);
  }
}
