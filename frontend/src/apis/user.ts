import request from "@/utils/request";

export const getUsers = async () => {
  try {
    const res = await request.get("/api/admin/user/")
    return res
  } catch (error) {
    console.error(error)
  }
}
