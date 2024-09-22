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
