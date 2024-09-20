import request from "@/utils/request";

export const getBlogList = async (searchParams: any) => {
  try {
    const res = await request.get("/api/blog/", {
      params: { page: searchParams.page, pageSize: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getBlogById = async (id: number) => {
  try {
    const res = await request.get("/api/blog/" + id, );
    return res;
  } catch (error) {
    console.error(error);
  }
};
