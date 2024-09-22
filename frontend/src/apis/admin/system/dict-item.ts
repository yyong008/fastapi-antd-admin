import request from "@/utils/request";

type TDict = {
  page: number;
  pageSize: number;
};

export const getDictItem = async (id: number, searchParams: TDict) => {
  try {
    const res = await request.get("/api/admin/system/dict-item/" + id, {
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
