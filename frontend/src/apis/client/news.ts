import request from "@/utils/request";

export const getNewsList = async (searchParams: any) => {
  try {
    const res = await request.get("/api/news/", {
      params: { page: searchParams.page, pageSize: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getNewsById = async (id: number) => {
  try {
    const res = await request.get("/api/news/" + id);
    return res;
  } catch (error) {
    console.error(error);
  }
};
