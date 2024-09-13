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
