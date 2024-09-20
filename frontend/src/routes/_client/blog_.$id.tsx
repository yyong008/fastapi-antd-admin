import { BlogContent } from "@/components/Client/BlogDetail/blog-content";
import { BlogHeader } from "@/components/Client/BlogDetail/blog-header";
import { createFileRoute } from "@tanstack/react-router";
import { getBlogById } from "@/apis/client/blog";

export const Route = createFileRoute("/_client/blog/$id")({
  component: BlogDetailRoute,
  async loader({ params }) {
    const result: any = await getBlogById(Number(params.id))
    if(result && result.code === 0) {
      return result.data
    }
  }
});

export function BlogDetailRoute() {
  const _data = Route.useLoaderData();
  const blog = _data;
  return (
    <div className="flex flex-col  w-[40vw] h-[80vh]">
      <BlogHeader blog={blog} />
      <BlogContent content={blog.content} />
    </div>
  );
}
